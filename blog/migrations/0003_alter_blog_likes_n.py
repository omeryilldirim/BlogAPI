# Generated by Django 4.2.2 on 2023-06-27 18:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_category_options_remove_blog_comment_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes_n',
            field=models.ManyToManyField(related_name='likes_n', to=settings.AUTH_USER_MODEL),
        ),
    ]
