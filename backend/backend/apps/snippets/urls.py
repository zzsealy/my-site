# from django.conf.urls import url, path
from django.urls import path, re_path
from ..snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    re_path('snippets/(?P<pk>[0-9]+)/', views.snippet_detail),
]
