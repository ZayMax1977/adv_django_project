from django.db import models
from django.urls import reverse

from all_adv.templates.all_adv.rubrics import SUB_RUBRICS


class Adv(models.Model):

    # -----------------Общие----------------------------------
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=50,verbose_name='Наименование', help_text='Это хелп')
    transaction = models.ForeignKey('Transaction',null=True,on_delete=models.PROTECT, verbose_name='Вид сделки')
    region = models.ForeignKey('Region', null=True, on_delete=models.PROTECT, verbose_name='Регион')

    city = models.CharField(max_length=50, verbose_name='Город',null=True)
    district_city = models.CharField(max_length=50, verbose_name='Район города',default='',blank =True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/',
                              null=True, blank=True)

    user_name = models.CharField(max_length=50, verbose_name='Имя',null=True)
    phone_number = models.CharField(max_length=50,null=True,  verbose_name='Телефон')
    content = models.TextField(null=True,  verbose_name='Описание')
    price = models.FloatField(null=True,blank =True,verbose_name='Цена')
    rubric = models.ForeignKey('Rubric',null=True,on_delete=models.PROTECT, verbose_name='Рубрика')
    subrubric = models.CharField(max_length=70,blank =True, null=True,choices=SUB_RUBRICS, verbose_name='Подрубрика')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано от')
    update = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено  от')


    # -----------------Для недвижимости----------------------------------

    street = models.CharField(max_length=50, verbose_name='Улица',blank =True,default='')
    floors = models.CharField(max_length=50,null=True,blank =True,verbose_name='Этажей')
    floor = models.CharField(max_length=50,null=True,blank =True,verbose_name='Этаж')
    rooms = models.CharField(max_length=50,null=True,blank =True,verbose_name='Комнат')
    square_rooms = models.FloatField(null=True,blank =True,verbose_name='Площадь комнат')
    square_land = models.FloatField(null=True,blank =True,verbose_name='Площадь земли')
    law_status = models.ForeignKey('LawStatus',blank =True,null=True,on_delete=models.PROTECT, verbose_name='Статус')
    ower = models.ForeignKey('Subject',null=True,blank =True,on_delete=models.PROTECT, verbose_name='Субъект')
    # -----------------Для авто----------------------------------
    car_mark = models.ForeignKey('CarMark',null=True,blank =True,on_delete=models.PROTECT, verbose_name='Марка')
    car_model = models.CharField(max_length=50, verbose_name='Модель',null=True,blank =True)
    car_year = models.CharField(max_length=50,null=True,blank =True,verbose_name='Год')
    car_fuel = models.ForeignKey('CarFuel',null=True,blank =True,on_delete=models.PROTECT, verbose_name='Топливо')

    car_color = models.CharField(max_length=50, verbose_name='Цвет',null=True,blank =True)
    car_body = models.ForeignKey('CarBody',null=True,on_delete=models.PROTECT, verbose_name='Кузов',blank =True)
    car_actuator = models.ForeignKey('CarActuator',null=True,on_delete=models.PROTECT, verbose_name='Привод',blank =True)
    car_transmission = models.ForeignKey('CarTransmission',null=True,on_delete=models.PROTECT, verbose_name='Коробка',blank =True)
    car_run = models.CharField(max_length=50,null=True,blank =True,verbose_name='Пробег')
    car_engine_capacity = models.FloatField(null=True,blank =True,verbose_name='Объем двигателя')

    # -----------------Для знакомства----------------------------------
    who = models.CharField(max_length=50, verbose_name='Кто',null=True,blank =True)
    whom = models.CharField(max_length=50, verbose_name='Кого',null=True,blank =True)
    your_age = models.CharField(max_length=50,null=True,blank =True,verbose_name='Возраст Ваш')
    intention_age = models.CharField(max_length=50,null=True,blank =True,verbose_name='Возраст поиска')
    intention = models.ForeignKey('Intention',null=True,on_delete=models.PROTECT, verbose_name='Намерение',blank =True)

    # -------------------для работа---------
    salary = models.CharField(max_length=50,null=True,blank =True,verbose_name='Зарплата от')
    mode = models.CharField(max_length=50, verbose_name='Режим работы',null=True,blank =True)

    def get_absolute_url(self):
        return reverse('by_rubric',kwargs={'rubric_id': self.rubric_id})

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

    def get_absolute_url(self):
        return reverse('by_rubric',kwargs={'rubric_id': self.id})
    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'

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

class LawStatus(models.Model):
    name = models.CharField(max_length=70,db_index=True,verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Статус'
        verbose_name = 'Статус'

class Subject(models.Model):
    name = models.CharField(max_length=70,db_index=True,verbose_name='Субъект')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Субъект'
        verbose_name = 'Субъект'

class CarFuel(models.Model):
    name = models.CharField(max_length=70,db_index=True,verbose_name='Топливо')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Топливо'
        verbose_name = 'Топливо'

class CarTransmission(models.Model):
    name = models.CharField(max_length=70,db_index=True,verbose_name='Коробка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Коробка'
        verbose_name = 'Коробка'

class CarActuator(models.Model):
    name = models.CharField(max_length=70,db_index=True,verbose_name='Привод')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Привод'
        verbose_name = 'Привод'

class CarBody(models.Model):
    name = models.CharField(max_length=70,db_index=True,verbose_name='Кузов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Кузов'
        verbose_name = 'Кузов'

class Intention(models.Model):
    name = models.CharField(max_length=70,db_index=True,verbose_name='Намерение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Намерение'
        verbose_name = 'Намерение'



