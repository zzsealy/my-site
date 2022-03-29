import os

from django.conf import settings
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.status import HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.response import Response
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


from backend.apps.blog.models import Category, Post as PostModel, Comment, PostImage
from backend.apps.blog.serializers import Cateserializer, Postserializer, CommentSerializer, PostImageSerializer
from backend.apps.accounts.models import User
from backend.apps.accounts.utils import login_expire



# Create your views here.


class CateList(APIView):
    def get(self, request):
        cates = Category.objects.all()
        serializer = Cateserializer(cates, many=True)
        return Response(serializer.data)

    @method_decorator(login_expire)
    def post(self, request):
        data = request.data
        cate_name = data.get('cate')
        if data.get("need_login", None):
            return Response(status=HTTP_401_UNAUTHORIZED)
        if cate_name:
            cate = Category(name=cate_name)
            cate.save()
            return Response({"status_code": HTTP_200_OK, "message": "添加成功"})


class Cate(APIView):
    def get(self, request):
        pass


    @method_decorator(login_expire)
    def delete(self, request, nid=None):
        del_cate = Category.objects.filter(id=nid).first()
        if del_cate:
            del_cate.delete()
            return Response({'message': '删除成功'})
        return Response({'message': '删除失败'})
    

    @method_decorator(login_expire)
    def put(self, request, nid):
        data = request.data
        cate = Category.objects.filter(id=nid).first()
        cate_name = data.get('cate_name')
        if cate:
            cate.name = cate_name
            cate.save()
            return Response({ "message": "修改成功" })
        return Response({ "message": "修改失败" })




class Postlist(APIView):
    
    def get(self, request):
        posts = PostModel.objects.all()
        serialzier = Postserializer(posts, many=True)
        for data in serialzier.data:
            data['created'] = data['created'].replace('T', ' ').split('.')[0]
        return Response(serialzier.data)

    def post(self, request):
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

    def get(self, request, id):
        if id:
            post = PostModel.objects.filter(id=id).first()
            seriialzer = Postserializer(post)
            res_data = seriialzer.data
            res_data['cate_id'] = post.cate.id
            return Response(res_data)


    @method_decorator(login_expire) 
    def post(self, request):
        data = request.data
        cate_id = data.get('cate_id')
        post_title = data.get('post_title')
        post_subhead = data.get('post_subhead')
        post_body = data.get('post_body')
        # 正常情况下 肯定都是存在的就直接用 get了
        try:
            cate = Category.objects.get(id=cate_id)
            post = PostModel(title=post_title, subhead=post_subhead, body=post_body, owner=request.user, cate=cate)
            post.save()
            return Response({"message": "成功"})
        except Exception as e:
            print("e:", e)


    def put(self, request, id):
        pass


    def delete(self, request):
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
