from django.db import models

class Adv(models.Model):
    title = models.CharField(max_length=50,verbose_name='Товар')
    #Если True, Django будет хранить пустые значения как NULL в базе данных. По умолчанию установлено значение False
    content = models.TextField(null=True,blank =True,verbose_name='Описание')
    #Если True, поле может быть пустым. По умолчанию установлено значение False.
    #Обратите внимание, что это отличается от null. null связана исключительно с базой данных, тогда как blank связана с проверкой. Если
    # поле имеет blank = True, проверка формы позволит ввести пустое значение. Если поле имеет blank = False, поле будет обязательным.
    price = models.FloatField(null=True,blank =True,verbose_name='Цена')
    rubric = models.ForeignKey('Rubric',null=True,on_delete=models.PROTECT, verbose_name='Рубрика')
    published = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Опубликовано от')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20,db_index=True,verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'



