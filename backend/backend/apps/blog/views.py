from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.status import HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.response import Response


from backend.apps.blog.models import Category, Post as PostModel, Comment, Image
from backend.apps.blog.serializers import Cateserializer, Postserializer, CommentSerializer, ImageSerializer
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
        print("cate_name========", cate_name)
        if cate:
            print("拿到了！！！！！！！")
            cate.name = cate_name
            cate.save()
            return Response({ "message": "修改成功" })
        return Response({ "message": "修改失败" })




class Postlist(APIView):
    pass



class Post(APIView):

    def get(self, request, id):
        post = PostModel.objects.get(id=id)
        serializer = Postserializer(post)
        return Response(serializer.data)


    @method_decorator(login_expire) 
    def post(self, request):
        data = request.data
        cate_id = data.get('cate_id')
        post_title = data.get('post_title')
        post_subhead = data.get('post_subhead')
        post_body = data.get('post_body')
        # 正常情况下 肯定都是存在的就直接用 get了
        try:
            print('data:', data)
            print("cate_id:", cate_id)
            cate = Category.objects.get(id=cate_id)
            post = PostModel(title=post_title, subhead=post_subhead, body=post_body, owner=request.user, cate=cate)
            post.save()
            print(data)
            return Response({"message": "成功"})
        except Exception as e:
            print("e:", e)


    def put(self, request, id):
        pass