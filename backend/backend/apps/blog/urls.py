from django.urls import path
from backend.apps.blog.views import All_articel, CateList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('articles', All_articel.as_view(), name='all_article'),
    path('categories', CateList.as_view(), name="categories")
])