from rest_framework import generics
from django.contrib.auth import logout
from django.http import  JsonResponse
from django.middleware.csrf import get_token
import json
from rest_framework.status import HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from .serializers import UserSerializer, UserLoginSerializer
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
            user_instance = serializer.create(validated_data=serializer.validated_data)
            if user_instance:
                return Response( data={ "status_code": StatusCode.OK.value, "message": "注册成功, 请登录"})
            else:
                return Response( data={ "status_code": StatusCode.ERROR.value, "message": '发生错误'})
        else:
            return Response( data={ "status_code": serializer.error_code, "message": serializer.error_message })
    

class LoginView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            return Response(data={'status_code': StatusCode.OK.value, 'message': '登陆成功', 'token': serializer.validated_data})
        else:
            return Response( data={"status_code": serializer.error_code, 'message': serializer.error_message })

