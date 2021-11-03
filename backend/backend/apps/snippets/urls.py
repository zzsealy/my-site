# from django.conf.urls import url, path
from django.urls import path, re_path
from ..snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight)
]

urlpatterns = format_suffix_patterns(urlpatterns)
