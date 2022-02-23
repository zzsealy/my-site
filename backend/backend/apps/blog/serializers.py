
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
    # cates = serializers.ManyRelatedField()
    class Meta:
        model = Post
        field = ('title', 'subhead', 'content', 'created', 'owner', 'cates')


class PostImageSerializer(serializers.ModelSerializer):
    owner_article = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = PostImage
        field = ('id', 'link')
    
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

