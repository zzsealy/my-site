from django.conf import settings

from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.status import HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.response import Response


from backend.apps.blog.models import Category, Post as PostModel, Comment, PostImage
from backend.apps.blog.serializers import Cateserializer, Postserializer, CommentSerializer, PostImageSerializer
from backend.apps.accounts.models import User
from backend.apps.accounts.utils import login_expire



# Create your views here.


class CateList(APIView):
    def get(self, request):
        cates = Category.objects.all()
        serializer = Cateserializer(cates, many=True)
        print(serializer.data)
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
    pass



class Post(APIView):

    def get(self, request, id):
        pass

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
            image.delete()
