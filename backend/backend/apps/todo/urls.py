
from django.urls import path
from todo.views import TodoLists, TodoList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    # path('', TodoLists.as_view(), name='todo_lists'),
    # path('todo_list/<int: id>', TodoList.as_view(), name='todo_list')
])