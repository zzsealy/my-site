
from rest_framework import generics
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
import json
from django.contrib.auth.hashers import check_password
from rest_framework.status import HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_200_OK
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from .serializers import UserSerializer
from .user_dal import user_dal

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
        print('jinlaile  ========== ')
        post_data = request.data
        username = post_data.get('username')
        password = post_data.get('password')
        repeat_password = post_data.get('passwordRepeat')
        if repeat_password != password:
            return Response( data={ "status_code": 401, "message": "两次密码不一致"})
        create_info = {'username': username, 'password': password}
        if user_dal.create_one_obj(create_info=create_info):
            return Response(data={ "status_code": 200, "message": "创建成功，请登录"})

class LoginView(APIView):
    authentication_classes = (TokenAuthentication,)
    
    def post(self, request, format=None):
        data = request.data
        username = data['username']
        password = data['password']
        if user_dal.check_password(username=username, password=password):
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



