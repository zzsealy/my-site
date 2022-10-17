from django.db import models
from accounts.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'category'


class Post(models.Model):
    title = models.CharField(max_length=50)
    subhead = models.TextField(default=None, max_length=100)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    cate = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'


class PostImage(models.Model):
    name = models.CharField(default=None, max_length=100)
    image = models.ImageField()
    link = models.CharField(default=None, max_length=100)

    class Meta:
        db_table = 'post_img'


class Comment(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    owner_article = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'  # 评论


class SentenceCate(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'sentence_cate'


class Sentence(models.Model):
    body = models.TextField()
    author = models.CharField(blank=True, null=True, max_length=50)
    create_time = models.DateField(auto_now_add=True)
    cate = models.ForeignKey(SentenceCate, related_name='sentences', on_delete=models.CASCADE)

    class Meta:
        db_table = 'sentence'









    
