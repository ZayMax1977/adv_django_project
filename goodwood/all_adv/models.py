from django.db import models

class Adv(models.Model):
    title = models.CharField(max_length=50,verbose_name='Товар')
    #Если True, Django будет хранить пустые значения как NULL в базе данных. По умолчанию установлено значение False
    content = models.TextField(null=True,blank =True,verbose_name='Описание')
    #Если True, поле может быть пустым. По умолчанию установлено значение False.
    #Обратите внимание, что это отличается от null. null связана исключительно с базой данных, тогда как blank связана с проверкой. Если
    # поле имеет blank = True, проверка формы позволит ввести пустое значение. Если поле имеет blank = False, поле будет обязательным.
    price = models.FloatField(null=True,blank =True,verbose_name='Цена')

    published = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Опубликовано от')

    class Meta:
        verbose_name_plural='Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

