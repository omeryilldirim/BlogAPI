from django.urls import path, include
from .views import UserView, UserCreateView
from rest_framework.routers import DefaultRouter

# 'users/ -->'
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]

# ---------- Router ----------
router = DefaultRouter()
router.register('register', UserCreateView)
router.register('', UserView)
urlpatterns += router.urls