from django.urls import path
from django.conf.urls import url, include
from todo.views import TodoLists, ChildTodoViewset
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.routers import DefaultRouter
api_router = DefaultRouter()
api_router.register(r'todo', ChildTodoViewset, basename='tag')
api_url_patterns = api_router.urls

urlpatterns = format_suffix_patterns([
    path('todo_lists', TodoLists.as_view(), name='todo_lists'),
    path('todo_lists/<int:id>', TodoLists.as_view(), name='todo_list'),
    # path('todo/<int:id>', ChildTodo.as_view(), name='child_todo')
    # url(r'v1', include(api_url_patterns, namespace='views'))
])