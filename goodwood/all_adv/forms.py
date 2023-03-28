# from django.forms import ModelForm
# from all_adv.models import Adv
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

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




class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.CharField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ("username", 'email', 'password1', 'password2',)






