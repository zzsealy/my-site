import os
from django.conf import settings
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from user.utils import login_require, login_expire


from blog.models import Category, Post as PostModel, Comment, PostImage, Verse, VerseCate
from blog.serializers import CateSerializer, PostSerializer, CommentSerializer, PostImageSerializer, VerseSerializer,\
    VerseCateSerializer




# Create your views here.


class CateList(APIView):
    def get(self, request):
        cates = Category.objects.all()
        serializer = CateSerializer(cates, many=True)
        return Response(serializer.data)

    @method_decorator(login_expire)
    def post(self, request):
        data = request.data
        serializer = CateSerializer(data=data)
        
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
                serializer = CateSerializer(cate)
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
            serializer = CateSerializer(instance=cate, data=data)
            if serializer.is_valid():
                cate = serializer.save()
            return Response(data={ "message": "修改成功", "name": cate.name }, status=HTTP_200_OK)
        return Response(data={ "message": "修改失败" }, status=HTTP_404_NOT_FOUND)




class PostList(APIView):
    
    def get(self, request):
        get_data = request.GET
        cate_name = get_data.get('cate')
        posts = PostModel.objects.all()
        if cate_name:
            posts = posts.filter(cate__name=cate_name)
        page = get_data.get('page') # 页数
        if page:
            page = int(page)
            post_account_each_page = int(get_data.get('page_size'))# 每页条目数
            post_index_start = (page-1)*post_account_each_page
            post_index_end = page*post_account_each_page
            posts = posts[post_index_start: post_index_end]
        serializer = PostSerializer(posts, many=True)
        for data in serializer.data:
            data['created'] = data['created'].replace('T', ' ').split('.')[0]
        return Response(serializer.data)

    def post(self, request): # 搜索框的搜索， 查询到是ES。
        try:
            data = request.data
            search_value = data.get('searchValue')
        except Exception as e:
            return Response({'search_result_list': []})


class PostPaging(APIView):

    def get(self, request): # 返回页数
        cate = request.GET.get('cate')
        if cate == 'all':
            posts = PostModel.objects.all()
        else:
            posts = PostModel.objects.filter(cate__name=cate)
        return Response({'post_count': posts.count()})


class Post(APIView):

    def get(self, request, id=None):
        if id:
            post = PostModel.objects.filter(id=id).first()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        return Response(status=HTTP_200_OK)

    """
    { 
        "body": "test body",
        "cate": 7,
        "subhead": "test",
        "title": "test head",
        "owner": 1
    }
    """
    def post(self, request):

        if login_require(request):
            return Response(status=HTTP_401_UNAUTHORIZED)
        data = request.data
        post_serializer = PostSerializer(data=data)
        if post_serializer.is_valid():
            post_serializer.save()
        return Response(status=HTTP_200_OK, data=post_serializer.data)


    def put(self, request, id):
        post = PostModel.objects.filter(id=id).first()
        serializer = PostSerializer(instance=post, data=request.data)
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



# class PostImageView(APIView):

#     """
#     后台定义前端上传图片到服务端的接口
#     """
#     def post(self, request):
#         image = request.FILES.get('image', None)
#         image_name = image.name


#         post_name_image = PostImage.objects.filter(name=image_name).first()
#         post_image_instance = PostImage(image=image)
#         link = '/media/' + str(post_image_instance.image)

        
    
#         post_image_instance.link = link
#         post_image_instance.name = image_name
#         post_image_instance.save()

#         # media_root = settings.MEDIA_ROOT
#         # # pillow 处理照片信息
#         # absolute_img_url = media_root + '/' + image_name
#         # im = Image.open(absolute_img_url)
#         # width = im.width
#         # height = im.height
#         # image = im.resize((int(width/2), int(height/2)))
#         # image.save(absolute_img_url)

#         print(request.data)
#         return Response({'url': link})
#         # return Response({'message': '图片名字已经存在'})

#     def delete(self, request):
#         name = request.data.get('name', '')
#         if name:
#             image = PostImage.objects.filter(name=name).last()
#             try:
#                 os.remove(settings.MEDIA_ROOT + '/' + image.name)
#                 image.delete()
#                 return Response({
#                     'status': 200,
#                     'message': '删除成功'
#                 })
#             except Exception as e:
#                 return Response({
#                     'status': 500,
#                     'message': '发生错误:{}'.format(e)
#                 })


class TimePostDataView(APIView):

    def get(self, request):
        get_data = request.GET
        posts = PostModel.objects.all().order_by('created')
        time_post_data = {}
        for post in posts:
            created_time = post.created
            year = created_time.year
            # post指的是文章
            post_data = {'id': post.id, 'title': post.title, 'date':  created_time.strftime('%Y-%m-%d')} 
            if year in time_post_data.keys():
                pass
            else:
                time_post_data[year] = []

            time_post_data[year].append(post_data)
        return Response({'time_post_data': time_post_data})



class VerseList(APIView):

    def get(self, request):
        get_data = request.GET
        cate = get_data.get('cate')
        if cate:
            verses = Verse.objects.filter(cate=cate)
        else:
            verses = Verse.objects.all()
        serializer = VerseSerializer(verses, many=True)
        return Response(serializer.data)



class VerseView(APIView):

    def get(self, request):
        pass


    def post(self, request):
        post_data = request.data
        serializer = VerseSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=HTTP_200_OK)

    def put(self, request, id):
        post_data = request.data
        serializer = VerseSerializer()
        try:
            serializer.update(id, post_data)
            return Response(status=HTTP_200_OK)
        except Exception as e:
            print("更新verse错误:", e)
            return Response(status=299)
    
    def delete(self, request, id):
        verse = Verse.objects.get(id=id)
        verse.delete()
        return Response(status=200)


@api_view(['GET'])
def VerseCateList(request):
    if request.method == 'GET':
        verse_cates = VerseCate.objects.all()
        serializer = VerseCateSerializer(verse_cates, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def VerseCateCreate(request):
    if request.method == 'POST':
        post_data = request.data
        serializer = VerseCateSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=HTTP_200_OK)


@api_view(['PUT']) 
def VerseCateEdit(request, id):
    if request.method == 'PUT':
        id_cate = VerseCate.objects.get(id=id)
        post_data = request.data
        name = post_data.get('name')
        cate = VerseCate.objects.filter(name=name).first() # 如果要修改的分类名字已经存在，就把当前cate下的所有的句子移动到要修改成的分类下。
        if cate:
            verses = Verse.objects.filter(cate=id_cate)
            for verse in verses:
                verse.cate = cate
                verse.save()
            id_cate.delete()
            return Response(status=250)
        else: # 只是修改分类名称
            id_cate.name = name
            id_cate.save()
            return Response(status=HTTP_200_OK)