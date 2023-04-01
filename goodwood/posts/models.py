from django.contrib.auth.models import User
from django.db import models

class PostList(models.Model):
    title = models.CharField(max_length=100,verbose_name='Заголовок',db_index=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    content = models.TextField(verbose_name='Текст')
    author = models.CharField(max_length=100,verbose_name='Автор',db_index=True)

    company = models.CharField(max_length=100, verbose_name='Компания', db_index=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name='Телефон', db_index=True, blank=True)
    city = models.CharField(max_length=100,verbose_name='Город',db_index=True)
    url_address = models.URLField(verbose_name='URL',blank=True, null=True)
    views = models.IntegerField(verbose_name='Просмотры',blank=True,null=True)
    published = models.DateTimeField(auto_now_add=True,verbose_name='Опубликовано от')
    like = models.ManyToManyField(User,related_name='postcomment', blank=True, null=True)

    reply = models.ForeignKey('self', null=True,related_name='reply_ok',on_delete=models.CASCADE,blank=True)

    def total_likes(self):
        return self.like.count()

    # def total_views(self):
    #     return self.views.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'
        ordering = ['-published']

class Category(models.Model):
    name = models.CharField(max_length=45, db_index=True, verbose_name='Категория')

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.name

# class Likes(models.Model):
#     name = models.BooleanField(verbose_name='Лайки')
#
#     class Meta:
#         verbose_name_plural = 'Лайки'
#         verbose_name = 'Лайк'

    # def __str__(self):
    #     return self.name