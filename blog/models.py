from django.db import models
from django.contrib.auth.models import User
import json

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.URLField(max_length=400, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    post_views = models.PositiveSmallIntegerField(default=0)
    likes_n = models.CharField(max_length=1024, blank=True, default='[]')

    def __str__(self):
        return self.title
    
    def set_likes_n(self, value):
        self.likes_n = json.dumps(value)

    def get_likes_n(self):
        return json.loads(self.likes_n)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username