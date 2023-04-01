# Generated by Django 4.1.7 on 2023-03-31 14:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_alter_postlist_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postlist',
            name='reply',
        ),
        migrations.AddField(
            model_name='postlist',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='postcomment', to=settings.AUTH_USER_MODEL),
        ),
    ]