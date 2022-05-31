import os
from django.conf import settings
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.status import HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from backend.apps.accounts.utils import login_require


from blog.models import Category, Post as PostModel, Comment, PostImage
from blog.serializers import Cateserializer, Postserializer, CommentSerializer, PostImageSerializer
from accounts.utils import login_expire



# Create your views here.


class CateList(APIView):
    def get(self, request):
        cates = Category.objects.all()
        serializer = Cateserializer(cates, many=True)
        return Response(serializer.data)

    @method_decorator(login_expire)
    def post(self, request):
        data = request.data
        serializer = Cateserializer(data=data)
        
        if login_require(request):
            return Response(status=HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            serializer.save()
            return Response({"status_code": HTTP_200_OK, "message": "添加成功"})


class Cate(APIView):
    def get(self, request, nid=None):
        if nid:
            cate = Category.objects.filter(id=nid).first()
            if cate:
                serializer = Cateserializer(cate)
                return Response(data=serializer.data, status=HTTP_200_OK)
            return Response(status=HTTP_404_NOT_FOUND, data={"message": "id不存在"})
        return Response(status=HTTP_200_OK)


    def delete(self, request, nid=None):
    
        if login_require(request):
            return Response(status=HTTP_401_UNAUTHORIZED)

        del_cate = Category.objects.filter(id=nid).first()
        if del_cate:
            del_cate.delete()
            return Response(status=HTTP_200_OK, data={'message': '删除成功'})
        return Response(status=HTTP_404_NOT_FOUND, data={'message': '删除失败'})
    

    def put(self, request, nid):

        if login_require(request):
            return Response(status=HTTP_401_UNAUTHORIZED)

        data = request.data
        cate = Category.objects.filter(id=nid).first()
        if cate:
            serializer = Cateserializer(instance=cate, data=data)
            if serializer.is_valid():
                cate = serializer.save()
            return Response(data={ "message": "修改成功", "name": cate.name }, status=HTTP_200_OK)
        return Response(data={ "message": "修改失败" }, status=HTTP_404_NOT_FOUND)




class Postlist(APIView):
    
    def get(self, request):
        posts = PostModel.objects.all()
        serialzier = Postserializer(posts, many=True)
        for data in serialzier.data:
            data['created'] = data['created'].replace('T', ' ').split('.')[0]
        return Response(serialzier.data)

    def post(self, request): # 搜索框的搜索， 查询到是ES。
        try:
            data = request.data
            search_value = data.get('searchValue')
            es = Elasticsearch()
            s = Search(using = es, index='post')
            q = Q("multi_match", query=search_value, fields=['title', 'subhead', 'body', 'cate'])
            res = s.query(q).execute()
            search_results_dict_list = res.to_dict()['hits']['hits']
            return Response({'search_result_list': search_results_dict_list})
        except Exception as e:
            return Response({'search_result_list': []})




class Post(APIView):

    def get(self, request, id=None):
        if id:
            post = PostModel.objects.filter(id=id).first()
            seriialzer = Postserializer(post)
            return Response(seriialzer.data)
        return Response(status=HTTP_200_OK)

    """
    { 
        "body": "testbody",
        "cate": 7,
        "subhead": "test",
        "title": "testhead",
        "owner": 1
    }
    """
    def post(self, request):

        if login_require(request):
            return Response(status=HTTP_401_UNAUTHORIZED)
        data = request.data
        postserializer = Postserializer(data=data)
        if postserializer.is_valid():
            postserializer.save()
        return Response(status=HTTP_200_OK, data=postserializer.data)


    def put(self, request, id):
        post = PostModel.objects.filter(id=id).first()
        serializer = Postserializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_200_OK, data={"message": "修改成功"})
        return Response(status=500)


    def delete(self, request):

        if login_require(request):
            return Response(status=HTTP_401_UNAUTHORIZED)

        id = request.data.get('id')
        post = PostModel.objects.filter(id=id).first()
        if post:
            post.delete()
            return Response({'message': '删除成功'})



class PostImageView(APIView):

    """
    后台定义前端上传图片到服务端的接口
    """
    def post(self, request):
        image = request.FILES.get('image', None)
        image_name = image.name
        post_name_image = PostImage.objects.filter(name=image_name).first()
        postimage_instance = PostImage(image=image)
        link = '/media/' + str(postimage_instance.image)
        postimage_instance.link = link
        postimage_instance.name = image_name
        postimage_instance.save()
        print(request.data)
        return Response({'url': link})
        # return Response({'message': '图片名字已经存在'})

    def delete(self, request):
        name = request.data.get('name', '')
        if name:
            image = PostImage.objects.filter(name=name).last()
            try:
                os.remove(settings.MEDIA_ROOT + '/' + image.name)
                image.delete()
                return Response({
                    'status': 200,
                    'message': '删除成功'
                })
            except Exception as e:
                return Response({
                    'status': 500,
                    'message': '发生错误:{}'.format(e)
                })
