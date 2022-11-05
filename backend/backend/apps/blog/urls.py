from django.urls import path
from blog.views import CateList, Cate, PostList, PostPaging, Post, PostImageView, TimePostDataView, SentenceList, SentenceView, \
    SentenceCateList, SentenceCateCreate, SentenceCateEdit
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('categories', CateList.as_view(), name="categories"),
    path('category/<int:nid>', Cate.as_view(), name="category"),
    path('posts', PostList.as_view(), name="posts"), # 所有post
    path('paging_data', PostPaging.as_view(), name='post_paging'), # 分页数据
    path('post', Post.as_view(), name='add_post_view'),
    path('post/<int:id>/', Post.as_view(), name='post_view'),
    path('postimage', PostImageView.as_view(), name='postimage-delete'),
    path('time_post_data', TimePostDataView.as_view(), name='time_post_data'),
    path('sentences', SentenceList.as_view(), name='sentences'), # 句子过滤分类 所有
    path('sentence', SentenceView.as_view(), name='sentence'), # 句子 增删改查
    path('sentence/<int:id>', SentenceView.as_view(), name='edit_sentence'),
    path('sentence_cates', SentenceCateList, name='sentence_cates'), # 句子类别的过滤，分类,所有 视图
    path('sentence_cate', SentenceCateCreate, name='create_sentence_cate'),
    path('sentence_cate/<int:id>', SentenceCateEdit, name='edit_sentence_cate')
])