from rest_framework import serializers
from .models import Category, Blog, Comment
import json


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    # category_id = serializers.IntegerField()
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    likes_n = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Blog
        exclude = []

    def create(self, validated_data):
        author = self.context['request'].user
        validated_data['author'] = author
        blog = Blog.objects.create(**validated_data)
        return blog
    
    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()

    def get_likes(self, obj):
        return len(json.loads(obj.likes_n))

    def get_likes_n(self, obj):
        return json.loads(obj.likes_n)

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = Comment
        exclude = []