import os, datetime
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from backend.utils.constants.status_code import StatusCode

from todo.serializers import TodoSerializer, TodoListSerializer, GetTodoListSerializer, ChangeTodoListSerializer

from todo.models import Todo, TodoList
# Create your views here.


class TodoLists(APIView):
    
    def get(self, request, id=None):
        if id:
            todo_list = TodoList.objects.get(id=id)
            serializers = GetTodoListSerializer(todo_list)
            return Response({'status_code':StatusCode.OK.value, 'todo_list':serializers.data})
        else:
            todo_lists = TodoList.objects.filter(user_id=request.user_id).order_by('-create_datetime')
            serializers = GetTodoListSerializer(todo_lists, many=True)
            return Response({'status_code':StatusCode.OK.value, 'todo_list':serializers.data, 'todo_list_num': len(todo_lists)})


    def post(self, request, id=None):
        user_id = request.user_id
        data = request.data
        if id:
            create_info = {
                'body': data.get('todoContent'),
                'list_id': id,
                'create_datetime': datetime.datetime.now()
            }
            serializer = TodoSerializer(data=create_info)
            if serializer.is_valid():
                if serializer.save():
                    todo_list = TodoList.objects.get(id=id)
                    one_todo_list_serializer = GetTodoListSerializer(todo_list)
                return Response({'status_code': StatusCode.OK.value, 'todo_list': one_todo_list_serializer.data, 'message': '创建成功'})
            return Response({'status_code': serializer.error_code, 'message': serializer.error_message})
        else:
            data['user_id'] = user_id
            data['expect_finish_date'] = data.pop('dateString')
            serializer = TodoListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response()
            return Response({'status_code': serializer.error_code, 'message': serializer.error_message})
    
    def put(self, request, id=None):
        if id:
            post_data = request.data
            todo_list = TodoList.objects.get(id=id)
            serializer = ChangeTodoListSerializer(instance=todo_list, data=post_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status_code': StatusCode.OK.value, 'message': '修改成功'})
            return Response({'status_code': serializer.error_code, 'message': serializer.error_message})


class ChildTodo(APIView):

    def delete(self, request, id):
        Todo.objects.get(id=id).delete()
        return Response({'status_code': StatusCode.OK.value, 'message': '修改成功'})
