from datetime import datetime
from django.forms.models import model_to_dict

from todo.models import Todo, TodoList
from backend.utils.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from backend.utils.constants.todo_constant import TagConstant

class TodoSerializer(Serializer):

    class Meta:
        model = Todo
        fields = '__all__'



class TodoListSerializer(ModelSerializer):
    user_id = serializers.IntegerField(required=False)
    tag = serializers.CharField(required=False)
    expect_finish_date = serializers.DateField(format='%Y-%m-%d', required=False)
    is_close = serializers.CharField(required=False)
    class Meta:
        model = TodoList
        fields = ('id', 'user_id', 'title', 'expect_finish_date', 'tag', 'is_close')
    
    def validate_user_id(self, obj):
        request = self.context.get('request')
        return request.user_id
    
    def validate_tag(self, tag):
        value = TagConstant[tag.upper()].value
        return value
        
    
    def validate_expect_finish_date(self, value):
        return value

    def validate_is_close(self, value):
        return value
    
    def validate(self, attrs):
        request = self.context.get('request')
        attrs['user_id'] = request.user_id
        return super().validate(attrs)

# class ChangeTodoListSerializer(ModelSerializer):
#     tag = serializers.CharField(required=False)
#     type = serializers.CharField(required=False)

#     class Meta:
#         model = TodoList
#         fields = ('tag', 'type')
    
#     def validate_tag(self, tag):
#         return TagConstant[tag.upper()].value
    
#     def validate_type(self, type):
#         if type == 'close':
#             return 1
#         return 0 
    
#     def validate(self, attrs):
#         attrs['is_close'] = attrs.pop('type')
#         return attrs

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
    

class GetTodoListSerializer(Serializer):
    id = serializers.IntegerField()
    tag = serializers.CharField()
    child_todo = serializers.SerializerMethodField()
    title = serializers.CharField()

    
    def get_child_todo(self, obj):
        list_id = obj.get('id')
        sub_todo = Todo.objects.filter(list_id=list_id)
        sub_todo_list = [model_to_dict(todo) for todo in sub_todo]
        for todo in sub_todo_list:
            todo['is_finish'] = True if todo['is_finish'] else False
            todo['content'] = todo.pop('body')
        return sub_todo_list
    
    def to_representation(self, instance):
        rep = super().to_representation(instance=instance)
        rep['date_string'] = instance.get('expect_finish_date')
        rep['tag'] = TagConstant(int(instance.get('tag'))).name.lower()
        rep['can_change'] = True if instance.get('is_close') == 0 else False
        return rep
    