from user.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from .user_dal import user_dal
from backend.utils.errors import ValidationErrorNew
from backend.utils.serializers import ModelSerializer
from backend.utils.constants.status_code import StatusCode


# class UserSerializer(serializers.ModelSerializer):
#     """
#     因为'snippets' 在用户模型中是一个反向关联关系。在使用 ModelSerializer 类时它默认不会被包含，所以我们需要为它添加一个显式字段。
#     """
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')

class UserSerializer(ModelSerializer):
    passwordRepeat = serializers.CharField()
    name = serializers.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'password', 'passwordRepeat', 'name')
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        repeat_password = data.get('passwordRepeat')
        create_info = {'username': username, 'password': password}
        if repeat_password != password:
            raise ValidationErrorNew(code=StatusCode.PASS_NOT_EQUAL.value)
        if user_dal.create_one_obj(create_info=create_info):
            return data
        else:
            raise serializers.ValidationError(code=300)
    
