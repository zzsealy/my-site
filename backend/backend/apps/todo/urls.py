from django.urls import path
from todo.views import TodoLists, ChildTodo
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('todo_lists', TodoLists.as_view(), name='todo_lists'),
    path('todo_lists/<int:id>', TodoLists.as_view(), name='todo_list'),
    path('todo/<int:id>', ChildTodo.as_view(), name='child_todo')
])