from django.urls import path
from blog.views import CateList, Cate, PostList, PostPaging, Post, TimePostDataView, VerseList, VerseView, \
    VerseCateList, VerseCateCreate, VerseCateEdit
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('categories', CateList.as_view(), name="categories"),
    path('category/<int:nid>', Cate.as_view(), name="category"),
    path('posts', PostList.as_view(), name="posts"), # 所有post
    path('paging_data', PostPaging.as_view(), name='post_paging'), # 分页数据
    path('post', Post.as_view(), name='add_post_view'),
    path('post/<int:id>/', Post.as_view(), name='post_view'),
    # path('postimage', PostImageView.as_view(), name='postimage-delete'),
    path('time_post_data', TimePostDataView.as_view(), name='time_post_data'),
    path('verses/', VerseList.as_view(), name='verses'), # 句子过滤分类 所有
    path('verse/', VerseView.as_view(), name='verse'), # 句子 增删改查
    path('verse/<int:id>/', VerseView.as_view(), name='edit_verse'),
    path('verse_cates/', VerseCateList, name='verse_cates'), # 句子类别的过滤，分类,所有 视图
    path('verse_cate', VerseCateCreate, name='create_verse_cate'),
    path('verse_cate/<int:id>', VerseCateEdit, name='edit_verse_cate')
])