# Generated by Django 4.1.7 on 2023-04-01 10:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0009_alter_postlist_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlist',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='postcomment', to=settings.AUTH_USER_MODEL),
        ),
    ]
