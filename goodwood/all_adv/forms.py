# from django.forms import ModelForm
# from all_adv.models import Adv
from django import forms
from django.core.exceptions import ValidationError

from .models import *
from all_adv.templates.all_adv.rubrics import SUB_RUBRICS

class AddAdvCommon(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['transaction'].empty_label = ''
    #     И тд

    class Meta:
        model = Adv
        fields = ['title','transaction','rubric','subrubric','region',
        'city','district_city','user_name','phone_number','content','photo','price']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'content': forms.Textarea(attrs={'cols':100,'rows':10}),
        #     и тд
        }

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data['phone_number']
    #
    #     if type(str) in phone_number:
    #     # if len(phone_number) > 11:
    #         raise ValidationError('Длина номера превышает допустимый')
    #     return phone_number
    #
    # # def clean_title(self):
    # #     title = self.cleaned_data['title']
    # #     if len(title) > 11:
    # #         raise ValidationError('Длина номера превышает допустимый')
    # #     return title




class AddAdvRealtyForm(forms.ModelForm):
    class Meta:
        model = Adv
        fields = ['title','transaction','rubric','subrubric','region',
        'city','district_city','user_name','phone_number','content','photo','price','street','floors',
        'floor','rooms','square_rooms','square_land','law_status','ower']
class AddAdvAutoForm(forms.ModelForm):
    class Meta:
        model = Adv
        fields = ['title','transaction','rubric','subrubric','region',
        'city','user_name','phone_number','content','photo','price','car_mark',
        'car_model',"car_year",'car_fuel','car_color',"car_body","car_actuator","car_transmission",
        "car_run","car_engine_capacity"]

class AddAdvMeettingForm(forms.ModelForm):
    class Meta:
        model = Adv
        fields = ['title','transaction','rubric','subrubric','region',
        'city','user_name','phone_number','content','photo',"who","whom",'your_age',"intention_age","intention"]


class AddAdvJobForm(forms.ModelForm):
    class Meta:
        model = Adv
        fields = ['title','transaction','rubric','subrubric','region',
        'city','district_city','user_name','phone_number','content','photo',"salary","mode"]


# class AddAdvCommon(forms.Form):
#     # сделать класс Css общий для всех полей
#     # def __init__(self, *args, **kwargs):
#     #     super(AddAdvCommon, self).__init__(*args, **kwargs)
#     #     for field in self.fields:
#     #         self.fields[field].widget.attrs.update({'class': 'form-input'})
#     # или отдельно через виджет в каждом поле ниже
#
#
#     title = forms.CharField(max_length=50,label='Заголовок')
#     transaction = forms.ModelChoiceField(queryset=Transaction.objects.all(),empty_label='',label='Вид сделки')
#     rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),label='Рубрика',empty_label='')
#     subrubric = forms.ChoiceField(choices=SUB_RUBRICS,label='Подрубрика')
#     region = forms.ModelChoiceField(queryset=Region.objects.all(),empty_label='',label='Регион')
#     city = forms.CharField(max_length=50,required=False,label='Город')
#     district_city = forms.CharField(max_length=50,required=False,label='Район города')
#     user_name = forms.CharField(max_length=50,label='Имя')
#     phone_number = forms.CharField(max_length=11,label='Номер телефона')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 200, 'rows': 10}),label='Текст')
#     price = forms.FloatField(required=False,label='Цена')
#
# class AddAdvRealtyForm(forms.Form):
#
#     title = forms.CharField(max_length=50,label='Заголовок')
#     transaction = forms.ModelChoiceField(queryset=Transaction.objects.all(),label='Вид сделки',empty_label='')
#     rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),label='Рубрика',empty_label='')
#     subrubric = forms.ChoiceField(choices=SUB_RUBRICS,label='Подрубрика')
#     region = forms.ModelChoiceField(queryset=Region.objects.all(),label='Регион',empty_label='')
#     city = forms.CharField(max_length=50,required=False,label='Город')
#     district_city = forms.CharField(max_length=50,required=False,label='Район города')
#     user_name = forms.CharField(max_length=50,label='Имя')
#     phone_number = forms.CharField(max_length=11,label='Номер телефона')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}),label='Текст')
#
#     price = forms.FloatField(required=False,label='Цена')
#     street = forms.CharField(max_length=50,required=False,label='Улица')
#     floors = forms.CharField(max_length=50,required=False,label='Количество этажей')
#     floor = forms.CharField(max_length=50,required=False,label='Этаж')
#     rooms = forms.CharField(max_length=50,required=False,label='Количество комнат')
#     square_rooms = forms.FloatField(required=False,label='Общая площадь')
#     square_land = forms.FloatField(required=False,label='Площадь земли')
#     law_status = forms.ModelChoiceField(queryset=LawStatus.objects.all(),required=False,label='Правовой статус объекта',empty_label='')
#     ower = forms.ModelChoiceField(queryset=Subject.objects.all(),required=False,label='Собственник/Агентство',empty_label='')
#
# class AddAdvAutoForm(forms.Form):
#     title = forms.CharField(max_length=50,label='Заголовок')
#     transaction = forms.ModelChoiceField(queryset=Transaction.objects.all(),label='Вид сделки',empty_label='')
#     rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),label='Рубрика',empty_label='')
#     subrubric = forms.ChoiceField(choices=SUB_RUBRICS,label='Подрубрика')
#     region = forms.ModelChoiceField(queryset=Region.objects.all(),label='Регион',empty_label='')
#     city = forms.CharField(max_length=50,required=False,label='Город')
#     user_name = forms.CharField(max_length=50,label='Имя')
#     phone_number = forms.CharField(max_length=11,label='Номер телефона')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),label='Текст')
#
#     price = forms.FloatField(required=False,label='Цена')
#     car_mark = forms.ModelChoiceField(queryset=CarMark.objects.all(),required=False,label='Марка авто',empty_label='')
#     car_model = forms.CharField(max_length=50,required=False,label='Модель')
#     car_year = forms.CharField(max_length=50,required=False,label='Год выпуска')
#     car_fuel = forms.ModelChoiceField(queryset=CarFuel.objects.all(),required=False,label='Вид топлива',empty_label='')
#     car_color = forms.CharField(max_length=50,required=False,label='Цвет')
#     car_body = forms.ModelChoiceField(queryset=CarBody.objects.all(),required=False,label='Кузов',empty_label='')
#     car_actuator = forms.ModelChoiceField(queryset=CarActuator.objects.all(),required=False,label='Привод',empty_label='')
#     car_transmission = forms.ModelChoiceField(queryset=CarTransmission.objects.all(),required=False,label='Коробка',empty_label='')
#     car_run = forms.CharField(max_length=50,required=False,label='Пробег')
#     car_engine_capacity = forms.FloatField(required=False,label='Объем двигателя')
#
# class AddAdvMeettingForm(forms.Form):
#     title = forms.CharField(max_length=50,label='Заголовок')
#     transaction = forms.ModelChoiceField(queryset=Transaction.objects.all(),label='Вид сделки',empty_label='')
#     rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),label='Рубрика',empty_label='')
#     subrubric = forms.ChoiceField(choices=SUB_RUBRICS,label='Подрубрика')
#     region = forms.ModelChoiceField(queryset=Region.objects.all(),label='Регион',empty_label='')
#     city = forms.CharField(max_length=50,required=False,label='Город')
#     user_name = forms.CharField(max_length=50,label='Имя')
#     phone_number = forms.CharField(max_length=11,label='Номер телефона')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),label='Текст')
#
#     who = forms.CharField(max_length=50,required=False,label='Кто ищет')
#     whom = forms.CharField(max_length=50,required=False,label='Кого ищет')
#     your_age = forms.CharField(max_length=50,required=False,label='Возраст ваш')
#     intention_age = forms.CharField(max_length=50,required=False,label='Возраст объекта(ов) поиска')
#     intention = forms.ModelChoiceField(queryset=Intention.objects.all(),required=False,label='Цель поиска',empty_label='')
#
# class AddAdvJobForm(forms.Form):
#         title = forms.CharField(max_length=255,label='Заголовок')
#         transaction = forms.ModelChoiceField(queryset=Transaction.objects.all(),label='Вид сделки',empty_label='')
#         rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),label='Рубрика',empty_label='')
#         subrubric = forms.ChoiceField(choices=SUB_RUBRICS,label='Подрубрика')
#         region = forms.ModelChoiceField(queryset=Region.objects.all(),label='Регион',empty_label='')
#         city = forms.CharField(max_length=50,required=False,label='Город')
#         user_name = forms.CharField(max_length=50,label='Имя')
#         phone_number = forms.CharField(max_length=11,label='Номер телефона')
#         content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),label='Текст')
#
#         salary = forms.CharField(max_length=50,required=False,label='Зарплата')
#         mode = forms.CharField(max_length=50,required=False,label='Режим работы')



