from datetime import datetime

from todo.models import Todo, TodoList
from backend.utils.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from backend.utils.constants.todo_constant import TagConstant

class TodoSerializer(Serializer):

    class Meta:
        model = Todo
        fields = '__all__'



class TodoListSerializer(ModelSerializer):
    tag = serializers.CharField()
    expect_finish_date = serializers.CharField()
    class Meta:
        model = TodoList
        fields = ('id', 'user_id', 'title', 'expect_finish_date', 'tag')
    
    def validate_tag(self, tag):
        value = TagConstant[tag.upper()].value
        return value
        
    
    def validate_expect_finish_date(self, value):
        return datetime.strptime(value, "%Y-%m-%d")
    
    def validate(self, attrs):
        return super().validate(attrs)
    

class GetTodoListSerializer(Serializer):
    id = serializers.IntegerField()
    tag = serializers.CharField()
    child_todo = serializers.SerializerMethodField()
    title = serializers.CharField()

    
    def get_child_todo(self, obj):
        return []