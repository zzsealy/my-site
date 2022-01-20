
# 序列化器例子
from asyncore import read
from dataclasses import field
from rest_framework import serializers
from backend.apps.blog.models import Category, Post, Comment, Image


class Cateserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class Postserializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    cate = serializers.ReadOnlyField(source='cate.name')
    class Meta:
        model = Post
        fields = ('title', 'subhead', 'body', 'created', 'owner', 'cate')


class ImageSerializer(serializers.ModelSerializer):
    owner_article = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Image
        fields = ('index', 'title', 'image', 'owner_article')


class CommentSerializer(serializers.ModelSerializer):
    owner_article = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        field = ('name', 'content', 'created', 'email', 'owner_article')

