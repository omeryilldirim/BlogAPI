from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    BlogViewSet,
    CommentViewSet,
)

# 'api/ ->'
router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('blogs', BlogViewSet, basename='blogs')
router.register('comments', CommentViewSet, basename='comments')
urlpatterns = router.urls