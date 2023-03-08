from django.db import models

from all_adv.templates.all_adv.rubrics import SUB_RUBRICS


class Adv(models.Model):


    is_active = models.BooleanField(default=False)
    title = models.CharField(max_length=50,verbose_name='Товар', help_text='Это хелп')
    content = models.TextField(null=True,blank =True,verbose_name='Описание')
    transaction = models.ForeignKey('Transaction',null=True,on_delete=models.PROTECT, verbose_name='Вид сделки')
    city = models.CharField(max_length=50, verbose_name='Город',null=True,blank =True)
    region = models.ForeignKey('Region',null=True,on_delete=models.PROTECT, verbose_name='Регион')
    user_name = models.CharField(max_length=50, verbose_name='Имя',null=True,blank =True)
    price = models.FloatField(null=True,blank =True,verbose_name='Цена')
    rubric = models.ForeignKey('Rubric',null=True,on_delete=models.PROTECT, verbose_name='Рубрика')
    subrubric = models.CharField(max_length=70, null=True,choices=SUB_RUBRICS, verbose_name='Подрубрика')

    phone_number = models.IntegerField(null=True,blank =True,verbose_name='Телефон')
    street = models.CharField(max_length=50, verbose_name='Улица',null=True,blank =True)
    floors = models.IntegerField(null=True,blank =True,verbose_name='Этажей')
    floor = models.IntegerField(null=True,blank =True,verbose_name='Этаж')
    rooms = models.IntegerField(null=True,blank =True,verbose_name='Комнат')
    square_rooms = models.FloatField(null=True,blank =True,verbose_name='Площадь комнат')
    square_land = models.FloatField(null=True,blank =True,verbose_name='Площадь земли')
    car_mark = models.ForeignKey('CarMark',null=True,on_delete=models.PROTECT, verbose_name='Марка')
    car_model = models.CharField(max_length=50, verbose_name='Модель',null=True,blank =True)
    car_year = models.IntegerField(null=True,blank =True,verbose_name='Год')

    car_color = models.CharField(max_length=50, verbose_name='Цвет',null=True,blank =True)
    published = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Опубликовано от')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=45,db_index=True,verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'

# class SubRubric(models.Model):
#     name = models.CharField(max_length=70,db_index=True,verbose_name='Подрубрика')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = 'Подрубрики'
#         verbose_name = 'Подрубрика'

class Transaction(models.Model):
    name = models.CharField(max_length=21,db_index=True,verbose_name='Вид сделки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Вид сделки'
        verbose_name = 'Вид сделки'

class Region(models.Model):
    name = models.CharField(max_length=70,db_index=True,verbose_name='Регион')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Регионы'
        verbose_name = 'Регион'

class CarMark(models.Model):
    name = models.CharField(max_length=70,db_index=True,verbose_name='Марка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Марки'
        verbose_name = 'Марка'



