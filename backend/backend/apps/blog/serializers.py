
# 序列化器例子
from asyncore import read
from dataclasses import field
from rest_framework import serializers
from backend.apps.blog.models import Category, Post, Comment, PostImage


class Cateserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class Postserializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    cate = serializers.ReadOnlyField(source='cate.name')
    # cates = serializers.ManyRelatedField()
    class Meta:
        model = Post
        fields = ('id', 'title', 'subhead', 'body', 'created', 'owner', 'cate')


class PostImageSerializer(serializers.ModelSerializer):
    owner_article = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = PostImage
        fields = ('id', 'link')
    
    def create(self, validated_data):
        link = validated_data.get('link')
        image_instance = PostImage.objects.create(link=link)
        image_instance.save()
        return image_instance
    


class CommentSerializer(serializers.ModelSerializer):
    owner_article = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        field = ('name', 'content', 'created', 'email', 'owner_article')

