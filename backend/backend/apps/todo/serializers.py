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
        fields = ('user_id', 'title', 'expect_finish_date', 'tag')
    
    def validate_tag(self, tag):
        value = TagConstant[tag.upper()].value
        return value
        
    
    def validate_expect_finish_date(self, value):
        return datetime.strptime(value, "%Y-%m-%d")
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    
    def create(self, validated_data):
        return super().create(validated_data)
