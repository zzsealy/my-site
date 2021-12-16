from backend.apps.accounts.models import User
from backend.apps.blog.serializers import Articelserializer
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from rest_framework.status import HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_200_OK
from backend.apps.blog.models import Category, Article, Comment, Image
from backend.apps.blog.serializers import Cateserializer, Articelserializer, CommentSerializer, ImageSerializer
from rest_framework.response import Response

# Create your views here.


class CateList(APIView):
    def get(self, request):
        print("进来了")
        cates = Category.objects.all()
        serializer = Cateserializer(cates, many=True)
        return Response(serializer.data)


    def post(self, request):
        print(request.POST  )


class All_articel(APIView):
    pass
