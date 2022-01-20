
from backend.apps.accounts.models import User
from .serializers import UserSerializer
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
# Create your views here.


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


class LoginView(APIView):
    authentication_classes = (TokenAuthentication,)
    
    def post(self, request, format=None):
        data = json.loads(request.body.decode('utf-8'))
        username = data['username']
        password = data['password']
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return Response ( {"status_code": HTTP_203_NON_AUTHORITATIVE_INFORMATION, "message": "用户名密码错误"} )
        if check_password(password, user.password):
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            token.save()
            return Response( data={ "status_code": HTTP_200_OK, "message": "登陆成功", 'token': token.key, 'user_id': user.id})
        else:
            return Response( data={"status_code": HTTP_203_NON_AUTHORITATIVE_INFORMATION, 'message': '账号密码不正确'})


# @login_expire()
def userLogout(request):
    logout(request)
    return JsonResponse( { "status_code": HTTP_200_OK, "message": "success"})


def getToken(request):
    token = get_token(request)
    return JsonResponse({"token": token})




