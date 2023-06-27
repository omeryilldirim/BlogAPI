from rest_framework import serializers
from .models import Category, Blog, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    # category_id = serializers.IntegerField()
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    likes_n = serializers.ListField(required=False, read_only=True)
    # likes = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        exclude = []

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()
    
    # def get_likes(self, obj):
    #     return obj.likes_n.count()


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = Comment
        exclude = []