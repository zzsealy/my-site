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
        todo_lists = TodoList.objects.all()
        serializers = TodoListSerializer(todo_lists, many=True)
        return Response(serializers.data)


    def post(request):
        pass