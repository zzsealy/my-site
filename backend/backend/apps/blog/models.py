from django.db import models
from backend.apps.accounts.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=50)
    subhead = models.TextField(default=None, max_length=100)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    cate = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)


class Image(models.Model):
    index = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField()
    owner_article = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)


class Comment(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    owner_article = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)





    