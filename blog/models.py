from django.db import models
from django.contrib.auth.models import User

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
    image = models.URLField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    post_views = models.PositiveSmallIntegerField(default=0)
    likes_n =models.ManyToManyField(User, related_name='likes_n', blank=True, null=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username