from user.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from .user_dal import user_dal
from backend.utils.errors import ValidationErrorNew
from backend.utils.serializers import ModelSerializer, Serializer
from backend.utils.constants.status_code import StatusCode
from user.utils import generation_token



class UserSerializer(ModelSerializer):
    passwordRepeat = serializers.CharField()
    name = serializers.CharField()
    
    class Meta:
        model = User
        fields = ('email', 'password', 'passwordRepeat', 'name')
    
    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        name = validated_data.get('name')
        create_info = {'email':email, 'password': password, 'nick_name': name}
        return user_dal.create_one_obj(create_info=create_info)
    
    def validate_email(self, email):
        user_email = user_dal.get_info_filters(filters={'email': email})
        if user_email:
            raise ValidationErrorNew(code=StatusCode.EMAIL_EXIST.value, detail='此邮箱已经被注册')
        return email

    
    def validate(self, data):
        password = data.get('password')
        repeat_password = data.get('passwordRepeat')
        email = data.get('email')
        if repeat_password != password:
            raise serializers.ValidationError(code=StatusCode.PASS_NOT_EQUAL.value, detail='两次密码输入不一致， 请重试')
        return data
    

class UserLoginSerializer(Serializer):
    email = serializers.CharField(label='文章目录')
    password = serializers.CharField(help_text='文章sss')

    # class Meta:
    #     sw
    
    def validate(self, attrs):

        email = attrs.get('email')
        password = attrs.get('password')
        user = user_dal.get_one_by_condition(condition={'email': email}) 
        if not user:
            raise serializers.ValidationError(code=StatusCode.USER_NOT_EXIST.value, detail='邮箱不存在')
        if user_dal.check_password(hash_password=user.get('password'), password=password):
            token = generation_token(user_id=user.get('id'))
            return token
        raise serializers.ValidationError(code=StatusCode.PASSWORD_ERROR.value, detail='密码错误')