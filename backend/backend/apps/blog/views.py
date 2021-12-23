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
        cates = Category.objects.all()
        serializer = Cateserializer(cates, many=True)
        print(serializer.data)
        return Response(serializer.data)


    def post(self, request):
        data = request.data
        cate_name = data.get('cate')
        if cate_name:
            cate = Category(name=cate_name)
            cate.save()
            return Response({"message": "添加成功"})


class Cate(APIView):
    def get(self, request):
        pass



    def delete(self, request, nid=None):
        del_cate = Category.objects.filter(id=nid).first()
        if del_cate:
            del_cate.delete()
            return Response({'message': '删除成功'})
        return Response({'message': '删除失败'})
    

    def put(self, request, nid):
        data = request.data
        cate = Category.objects.filter(id=nid).first()
        cate_name = data.get('cate_name')
        if cate:
            cate.name = cate_name
            cate.save()
            return Response({ "message": "修改成功" })
        return Response({ "message": "修改失败" })




class All_articel(APIView):
    pass
