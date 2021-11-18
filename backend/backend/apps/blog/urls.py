from django.urls import path
from backend.apps.blog.views import All_articel
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('articles', views.All_articel.as_view(), name='all_article'),
])