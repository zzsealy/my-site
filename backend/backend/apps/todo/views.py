import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from rest_framework.response import Response

from todo.serializers import TodoSerializer, TodoListSerializer

from todo.models import Todo, TodoList
# Create your views here.


class TodoLists(APIView):
    
    def get(self, request):
        todo_lists = TodoList.objects.all().order_by('-create_datetime')
        serializers = TodoListSerializer(todo_lists, many=True)
        return Response(serializers.data)


    def post(self, request):
        user_id = request.user_id
        data = request.data
        data['user_id'] = user_id
        data['expect_finish_date'] = data.pop('dateString')
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response({'status_code': serializer.error_code, 'message': serializer.error_message})

class TodoListView(APIView):

    def get(self, request, id):
        todo_list = TodoList.objects.get(id=id)
        serializer = TodoSerializer(todo_list)
        return Response(serializer.data)