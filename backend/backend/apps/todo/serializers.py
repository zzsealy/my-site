from rest_framework import serializers
from todo.models import Todo, TodoList


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'



class TodoListSerializer(serializers.ModelSerializer):
    child_todo = serializers.ReadOnlyField()

    class Meta:
        model = TodoList
        fields = ('id', 'all_finish', 'create_datetime', 'can_change', 'finish_rate', 'child_todo')
