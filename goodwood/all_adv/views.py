
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
    advs = Adv.objects.filter(is_active='True')
    rubrics = Rubric.objects.all()
    context ={
        "advs": advs,
        "rubrics":rubrics,
        'SUB_RUBRICS_ARR': SUB_RUBRICS_ARR,
        'RUBRIC_ARR': RUBRIC_ARR,
        'arr': [],
        'menu': menu,
        'page':'all_advs'
    }

    return render(requests,template_name='all_adv/all_advs.html', context=context)

def find_by_filter(requests):
    if requests.method == 'GET':
        print(requests.GET)
        return HttpResponseRedirect('/all_adv/')
    else:
        print('Не прошло')
        return render(requests,'all_advs.html')
    # if request.method == 'POST':
    #     form = AdvForm(request.POST)
    #     if form.is_valid():
    #
    #         print(form.cleaned_data['my_form_field_name'])
    #
    #         return HttpResponseRedirect('/all_adv/')
    # else:
    #     form = AdvForm()  # An unbound form
    #
    # return render_to_response('create_form.html', {
    #     'form': form,
    # })

def adv(requests,adv_id):

    adv = Adv.objects.get(pk=adv_id)
    rubrics = Rubric.objects.all()
    # current_rubric = Rubric.objects.get(pk=adv_id)
    context = {
        'adv': adv,
        'rubrics': rubrics,
        'SUB_RUBRICS_ARR': SUB_RUBRICS_ARR,
        'RUBRIC_ARR': RUBRIC_ARR,
        'menu': menu,
        'page': 'all_advs',
        # 'current_rubric': current_rubric
    }
    return render(requests,'all_adv/adv.html',context)



def by_rubric(requests,rubric_id):
    advs_by_rub = Adv.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'advs_by_rub':advs_by_rub,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
        'SUB_RUBRICS_ARR': SUB_RUBRICS_ARR,
        'RUBRIC_ARR': RUBRIC_ARR,
        'menu': menu,
        'page': 'all_advs',
    }
    return render(requests,'all_adv/by_rubric.html',context)

def by_subrubric(requests,subrubric):
    advs_by_subrub = Adv.objects.filter(subrubric=subrubric)
    rubrics = Rubric.objects.all()
    current_rubric_for_find =''
    for key in RUBRIC_ARR_FOR_FIND:
        if subrubric in key:
            current_rubric_for_find = key[subrubric]

    context = {
        'advs_by_subrub':advs_by_subrub,
        'SUB_RUBRICS_ARR': SUB_RUBRICS_ARR,
        'RUBRIC_ARR': RUBRIC_ARR,
        'rubrics': rubrics,
        # 'current_rubric': requests.GET['rubricName'],
        'current_rubric_for_find' : current_rubric_for_find,
        'menu': menu,
        'page': 'all_advs',
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

        return context

def interesting(requests):
    pass

def contact(requests):
    pass

def log(requests):
    pass

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
