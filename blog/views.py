from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Category, CategorySerializer,
    Blog, BlogSerializer,
    Comment, CommentSerializer
)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    