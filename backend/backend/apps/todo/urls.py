
from django.urls import path
from todo.views import TodoLists
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', TodoLists.as_view(), name='todo_lists')
])