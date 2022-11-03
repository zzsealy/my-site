from email.policy import default
from django.db import models
from accounts.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'post_category'

class Post(models.Model):
    title = models.CharField(max_length=50)
    subhead = models.TextField(default=None, max_length=100)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    owner_id = models.IntegerField(default=0)  # 作者id 
    cate_id = models.IntegerField(default=0)   # 类型id

    class Meta:
        db_table = 'post'


class PostImage(models.Model):
    name = models.CharField(default=None, max_length=100)
    image = models.ImageField()
    link = models.CharField(default=None, max_length=100)

    class Meta:
        db_table = 'post_image'

class Comment(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    owner_article = models.IntegerField(default=0)  # 所属的文章

    class Meta:
        db_table = 'comment'

class SentenceCate(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'sentence_cate'

class Sentence(models.Model):
    body = models.TextField()
    author = models.CharField(blank=True, null=True, max_length=50)
    create_time = models.DateField(auto_now_add=True)
    cate_id = models.IntegerField(default=0)  # 短句的分类id

    class Meta:
        db_table = 'sentence'







    