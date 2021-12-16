
# 序列化器例子
from asyncore import read
from dataclasses import field
from rest_framework import serializers
from backend.apps.blog.models import Category, Article, Comment, Image


class Cateserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fileds = ('cate')


class Articelserializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # cates = serializers.ManyRelatedField()
    class Meta:
        model = Article
        field = ('title', 'content', 'created', 'owner', 'cates')


class ImageSerializer(serializers.ModelSerializer):
    owner_article = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Image
        field = ('index', 'title', 'image', 'owner_article')


class CommentSerializer(serializers.ModelSerializer):
    owner_article = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        field = ('name', 'content', 'created', 'email', 'owner_article')

