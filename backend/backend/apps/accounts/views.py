
from backend.apps.accounts.models import User
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from rest_framework.status import HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_200_OK
from django.contrib.auth.decorators import login_required
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


def login(request):
    username = request.POST.data['username']
    password = request.POST.data['password']
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return JsonResponse ( {"status_code": HTTP_203_NON_AUTHORITATIVE_INFORMATION, "message": "用户不存在"} )
    if check_password(password, user.password):
        login(request, user)
        return JsonResponse( { "status_code": HTTP_200_OK, "message": "success"})


# @login_required()
def logout(request):
    logout(request)
    return JsonResponse( { "status_code": HTTP_200_OK, "message": "success"})




