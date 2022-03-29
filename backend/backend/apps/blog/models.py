from django.db import models
from accounts.models import User


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


class PostImage(models.Model):
    name = models.CharField(default=None, max_length=100)
    image = models.ImageField()
    link = models.CharField(default=None, max_length=100)


class Comment(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    owner_article = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)





    