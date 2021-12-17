from django.urls import path
from backend.apps.blog.views import All_articel, CateList, Cate
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('articles', All_articel.as_view(), name='all_article'),
    path('categories', CateList.as_view(), name="categories"),
    path('category', Cate.as_view(), name="category"),
])