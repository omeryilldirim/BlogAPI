# Generated by Django 4.2.2 on 2023-06-29 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blog_likes_n_blog_likes_n'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes_n',
            field=models.CharField(blank=True, default='[]', max_length=1024, null=True),
        ),
    ]