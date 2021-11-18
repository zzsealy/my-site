from backend.apps.accounts.models import User
from backend.apps.blog.serializers import articelseializer
from rest_framework import generics
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from rest_framework.status import HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_200_OK

# Create your views here.


class All_articel():
    pass
