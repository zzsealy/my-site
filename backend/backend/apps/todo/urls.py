from django.urls import path
from django.conf.urls import include
from todo.views import TodoLists, ChildTodoViewset
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.routers import DefaultRouter
todo_list_router = DefaultRouter()
todo_list_router.register('todo', ChildTodoViewset, basename='todo')
todo_list_router.register('todo_list', TodoLists, basename='todo_list')

urlpatterns = [
    path('', include(todo_list_router.urls)),
]