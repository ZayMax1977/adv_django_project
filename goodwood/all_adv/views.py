
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import inspect
from django.views.generic import CreateView

from all_adv.forms import AdvForm
from all_adv.models import Adv, Rubric
from all_adv.templates.all_adv.rubrics import SUB_RUBRICS_ARR, RUBRIC_ARR, RUBRIC_ARR_FOR_FIND

menu = [
    {'title': 'Главная','page_url':'index'},
    {'title': 'Объявления', 'page_url': 'all_advs'},
    {'title': 'Подать', 'page_url': 'add'},
    {'title': 'Интересно', 'page_url': 'interesting'},
    {'title': 'Контакты', 'page_url': 'contact'},
    {'title': 'Регистрация', 'page_url': 'log'},

]
def all_advs(requests):
    advs = Adv.objects.all()
    context ={
        'advs': advs,
        'SUB_RUBRICS_ARR': SUB_RUBRICS_ARR,
        'RUBRIC_ARR': RUBRIC_ARR,
        'arr': [],
        'menu': menu,
        'page':'all_advs',
        'title': 'GoodWood. Все объявления'
    }

    return render(requests,template_name='all_adv/all_advs.html', context=context)

def find_by_filter(requests):
    if requests.method == 'GET':
        print(requests.GET)
        return HttpResponseRedirect('/all_adv/')
    else:
        print('Не прошло')
        return render(requests,'all_advs.html')

def adv(requests,adv_id):
    adv = Adv.objects.get(pk=adv_id)
    context = {
        'adv': adv,
        'SUB_RUBRICS_ARR': SUB_RUBRICS_ARR,
        'RUBRIC_ARR': RUBRIC_ARR,
        'menu': menu,
        'page': 'all_advs',
        'title': 'GoodWood. Объявление',
    }
    return render(requests,'all_adv/adv.html',context)



def by_rubric(requests,rubric_id):
    advs_by_rub = Adv.objects.filter(rubric=rubric_id)
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'advs_by_rub':advs_by_rub,
        'current_rubric': current_rubric,
        'SUB_RUBRICS_ARR': SUB_RUBRICS_ARR,
        'RUBRIC_ARR': RUBRIC_ARR,
        'menu': menu,
        'page': 'all_advs',
        'title': 'GoodWood. По рубрикам'
    }
    return render(requests,'all_adv/by_rubric.html',context)

def by_subrubric(requests,subrubric):
    advs_by_subrub = Adv.objects.filter(subrubric=subrubric)
    current_rubric_for_find =''
    for key in RUBRIC_ARR_FOR_FIND:
        if subrubric in key:
            current_rubric_for_find = key[subrubric]

    context = {
        'advs_by_subrub':advs_by_subrub,
        'SUB_RUBRICS_ARR': SUB_RUBRICS_ARR,
        'RUBRIC_ARR': RUBRIC_ARR,
        'current_rubric_for_find' : current_rubric_for_find,
        'menu': menu,
        'page': 'all_advs',
        'title': 'GoodWood. По подрубрикам'
        }

    return render(requests,'all_adv/by_subrubric.html',context)

class AdvCreateView(CreateView):
    template_name = 'all_adv/create_form.html'
    form_class = AdvForm
    success_url = reverse_lazy("all_advs")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['menu'] = menu
        context['page'] = 'add'
        context['title'] = 'GoodWood. Добавить объявление'

        return context

def interesting(requests):
    return HttpResponse('Вкладка: Интересно')

def contact(requests):
    return HttpResponse('Вкладка: Контакты')

def log(requests):
    return HttpResponse('Вкладка: Вход')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
