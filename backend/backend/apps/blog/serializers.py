
# 序列化器例子
from asyncore import read
from dataclasses import field
from rest_framework import serializers
from blog.models import Category, Post, Comment, PostImage, Verse, VerseCate
from accounts.models import User


class CateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):

    """
    传入的外键id值,自动取到实例。
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'subhead', 'body', 'created', 'owner_id', 'cate_id')


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



class VerseSerializer(serializers.ModelSerializer):


    class Meta:
        model = Verse
        fields = "__all__"

    def update(self, id, update_info):
        update_info['cate'] = VerseCate.objects.get(id=update_info['cate'])
        Verse.objects.filter(id=id).update(**update_info)
    


class VerseCateSerializer(serializers.ModelSerializer):

    class Meta:
        model = VerseCate
        fields = "__all__"

