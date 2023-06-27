from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS
from .permissions import CustomBlogsPermission,CustomCommentPermission
from .serializers import (
    Category, CategorySerializer,
    Blog, BlogSerializer,
    Comment, CommentSerializer
)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Authenticated users can list or retrieve, but staff can create, update, or delete.
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAdminUser()]


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [CustomBlogsPermission]

    def get_queryset(self):
        if self.request.query_params.get('author', None):
            author = self.request.query_params.get('author')
            return Blog.objects.filter(author_id=author)
        return super().get_queryset()

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CustomCommentPermission]