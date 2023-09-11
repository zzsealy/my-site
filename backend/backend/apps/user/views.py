from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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

    @swagger_auto_schema(request_body=UserSerializer)
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
    
    @swagger_auto_schema(request_body=UserLoginSerializer, responses={})
    def post(self, request):
        """
        **status_code**
        4004 邮箱不存在
        4003 密码不对
        """
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            return Response(data={'status_code': StatusCode.OK.value, 'message': '登陆成功', 'token': serializer.validated_data})
        else:
            return Response( data={"status_code": serializer.error_code, 'message': serializer.error_message })


class UserInfo(APIView):
    
    def get(self, request):
        user_id = request.user_id
        user = User.objects.get(id=user_id)
        return Response(data={'status_code':StatusCode.OK.value, 'id':user.id, 'name': user.nick_name})