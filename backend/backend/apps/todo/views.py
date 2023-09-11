import os, datetime
from django.conf import settings
from django.core.paginator import Paginator
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.utils.constants.status_code import StatusCode
from backend.utils.constants.todo_constant import TagConstant, StatusConstant

from todo.serializers import TodoSerializer, TodoListSerializer, GetTodoListSerializer, ChangeTodoListSerializer

from todo.models import Todo, TodoList
# Create your views here.


class TodoLists(APIView):
    
    def get(self, request, id=None):
        if id:  # 获取单独的todo_list
            todo_list = TodoList.objects.get(id=id)
            serializers = GetTodoListSerializer(todo_list)
            return Response({'status_code':StatusCode.OK.value, 'todo_list':serializers.data})
        else:  # 获取todo_list列表
            tag = request.query_params.get('tag')
            status = request.query_params.get('status')
            todo_lists = TodoList.objects.filter(user_id=request.user_id).order_by('-create_datetime')
            total_lists_num = len(todo_lists)
            if tag:
                tag = TagConstant[tag.upper()].value
                todo_lists = todo_lists.filter(user_id=request.user_id, tag=tag).order_by('-create_datetime')
            if status:
                status = StatusConstant[status.upper()].value
                todo_lists = todo_lists.filter(user_id=request.user_id, is_close=status).order_by('-create_datetime')
            total_lists_num = len(todo_lists)
            page = request.query_params.get('page')
            if page:
                todo_lists = self.chunk_todo_list(todo_lists=todo_lists, page=page)
            serializers = GetTodoListSerializer(todo_lists, many=True)
            return Response({'status_code':StatusCode.OK.value, 'todo_list':serializers.data, 'todo_list_num': total_lists_num})

    def chunk_todo_list(self, todo_lists:[list], page: int):
        paginator = Paginator(todo_lists, 18)
        try:
            return paginator.page(page)
        except:
            return todo_lists

    def post(self, request, id=None):
        user_id = request.user_id
        data = request.data
        data['user_id'] = user_id
        data['expect_finish_date'] = data.pop('dateString')
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response({'status_code': serializer.error_code, 'message': serializer.error_message})
    
    def put(self, request, id=None):
        if id:  # 修改todo_list的标签
            post_data = request.data
            todo_list = TodoList.objects.get(id=id)
            serializer = ChangeTodoListSerializer(instance=todo_list, data=post_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status_code': StatusCode.OK.value, 'message': '修改成功'})
            return Response({'status_code': serializer.error_code, 'message': serializer.error_message})
    
    def delete(self, request, id):
        TodoList.objects.get(id=id).delete()
        return Response({'status_code': StatusCode.OK.value, 'message': '删除成功'})




class ChildTodoViewset(
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):


    def get_queryset(self):
        list_id = self.request.data.get('list_id')
        if list_id is not None:
            queryset = Todo.objects.filter(list_id=list_id)
        else:
            queryset = Todo.objects.all()
        return queryset

    def list(self, request, list_id):
        queryset = Todo.objects.filter(list_id=list_id)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        Todo.objects.get(id=id).delete()
        return Response({'status_code': StatusCode.OK.value, 'message': '修改成功'})
    
    def create(self, request):
        data = request.data
        list_id = data.get('list_id')
        create_info = {
            'body': data.get('todoContent'),
            'list_id': list_id,
            'create_datetime': datetime.datetime.now()
        }
        serializer = TodoSerializer(data=create_info)
        if serializer.is_valid():
            if serializer.save():
                todo_list = TodoList.objects.get(id=list_id)
                one_todo_list_serializer = GetTodoListSerializer(todo_list)
            return Response({'status_code': StatusCode.OK.value, 'todo_list': one_todo_list_serializer.data, 'message': '创建成功'})
        return Response({'status_code': serializer.error_code, 'message': serializer.error_message})
    
    
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, args, kwargs)
        return Response({'status_code': StatusCode.OK.value})

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.is_finish = 0 if obj.is_finish == 1 else 1
        obj.save()
        return Response({'status_code': StatusCode.OK.value})

    
