from django.urls import path
from backend.apps.blog.views import CateList, Cate, Postlist, Post
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('categories', CateList.as_view(), name="categories"),
    path('category/<int:nid>', Cate.as_view(), name="category"),
    path('posts', Postlist.as_view(), name="posts"),
    path('post', Post.as_view(), name='add_post_view'),
    path('post/<int:id>', Post.as_view(), name='post_view')
])