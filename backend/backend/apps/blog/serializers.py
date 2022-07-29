
# 序列化器例子
from asyncore import read
from dataclasses import field
from rest_framework import serializers
from blog.models import Category, Post, Comment, PostImage, Sentence, SentenceCate
from accounts.models import User


class Cateserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class Postserializer(serializers.ModelSerializer):
    cate = serializers.ReadOnlyField(source = 'cate.name')

    """
    传入的外键id值,自动取到实例。
    """
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
        fields = ('name', 'content', 'created', 'email', 'owner_article')



class SentenceSerializer(serializers.ModelSerializer):
    cate_name = serializers.ReadOnlyField(source='cate.name')
    class Meta:
        model = Sentence
        fields = "__all__"


class SentenceCateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SentenceCate
        fields = "__all__"

