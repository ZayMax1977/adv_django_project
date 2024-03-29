# Generated by Django 4.1.7 on 2023-03-31 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=45, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='PostList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Заголовок')),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('content', models.TextField(verbose_name='Текст')),
                ('author', models.CharField(db_index=True, max_length=100, verbose_name='Автор')),
                ('company', models.CharField(blank=True, db_index=True, max_length=100, verbose_name='Компания')),
                ('phone', models.CharField(blank=True, db_index=True, max_length=100, verbose_name='Телефон')),
                ('city', models.CharField(db_index=True, max_length=100, verbose_name='Город')),
                ('url_address', models.URLField(verbose_name='URL')),
                ('views', models.IntegerField(verbose_name='Просмотры')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано от')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='posts.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-published'],
            },
        ),
    ]
