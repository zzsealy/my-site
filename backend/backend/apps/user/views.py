from rest_framework import generics
from django.contrib.auth import logout
from django.http import  JsonResponse
from django.middleware.csrf import get_token
import json
from rest_framework.status import HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from .serializers import UserSerializer
from .user_dal import user_dal
from user.utils import generation_token
from backend.utils.constants.status_code import StatusCode
"""
我们只想将用户展示成只读视图，
因此我们将使用ListAPIview和RetryeveAPIView通用的
基于类的视图
"""

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegister(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return Response( data={ "status_code": StatusCode.OK.value, "message": "注册成功, 请登录"})
        else:
            return Response( data={ "status_code": StatusCode.PASS_NOT_EQUAL, "message": "两次密码不一致"})

class LoginView(APIView):
    
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user = user_dal.get_one_by_condition(condition={'username': username}) 
        if user and user_dal.check_password(hash_password=user.get('password'), password=password):
            return Response( data={ "status_code": HTTP_200_OK, "message": "登陆成功"})
        else:
            return Response( data={"status_code": 400, 'message': '账号密码不正确'})
    


# @login_expire()
def userLogout(request):
    logout(request)
    return JsonResponse( { "status_code": HTTP_200_OK, "message": "success"})


def getToken(request):
    token = get_token(request)
    return JsonResponse({"token": token})



