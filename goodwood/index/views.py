from django.http import HttpResponse
from django.shortcuts import render

menu = [
    {'title': 'Главная','page_url':'index'},
    {'title': 'Объявления', 'page_url': 'all_advs'},
    {'title': 'Подать', 'page_url': 'add'},
    # {'title': 'Интересно', 'page_url': 'interesting'},
    {'title': 'Контакты', 'page_url': 'contact'},
    {'title': 'Регистрация', 'page_url': 'register'},
    {'title': 'Вход', 'page_url': 'login'},

]
def index(requests):
    context = {
        'menu': menu,
        'page': 'index',
        'title': 'GoodWood. Главная'
    }
    return render(requests,'index/index.html',context)
