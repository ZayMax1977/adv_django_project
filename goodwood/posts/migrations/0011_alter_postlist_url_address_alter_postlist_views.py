# Generated by Django 4.1.7 on 2023-04-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_postlist_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlist',
            name='url_address',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='postlist',
            name='views',
            field=models.IntegerField(blank=True, null=True, verbose_name='Просмотры'),
        ),
    ]