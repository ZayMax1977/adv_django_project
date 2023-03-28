
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from all_adv.forms import AddAdvRealtyForm, AddAdvAutoForm, AddAdvCommon, AddAdvMeettingForm, AddAdvJobForm
from all_adv.models import Adv, Rubric
from all_adv.templates.all_adv.rubrics import SUB_RUBRICS_ARR, RUBRIC_ARR, RUBRIC_ARR_FOR_FIND
from .utils import *

class AllAdvs(DataMixin,ListView):
    model = Adv
    template_name = 'all_adv/all_advs.html'
    context_object_name = 'advs'



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        send_to_mixin = self.get_user_context(title = 'GoodWood. Все объявления')
        context = dict(list(context.items()) + list(send_to_mixin.items()))
        return context

    def get_queryset(self):

        return Adv.objects.filter(is_active=True)



class ByRubric(DataMixin,ListView):
    model = Adv
    template_name = 'all_adv/by_rubric.html'
    context_object_name = 'advs_by_rub'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        send_to_mixin = self.get_user_context(title='GoodWood. По рубрикам',current_rubric = Rubric.objects.get(pk=self.kwargs['rubric_id']))
        context = dict(list(context.items()) + list(send_to_mixin.items()))
        return context

    def get_queryset(self):
        return Adv.objects.filter(rubric_id=self.kwargs['rubric_id'],is_active=True)

class BySubRubric(DataMixin,ListView):
    model = Adv
    template_name = 'all_adv/by_subrubric.html'
    context_object_name = 'advs_by_subrub'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_rubric_for_find = ''
        for key in RUBRIC_ARR_FOR_FIND:
            if self.kwargs['subrubric'] in key:
                current_rubric_for_find = key[self.kwargs['subrubric']]

        send_to_mixin = self.get_user_context(title='GoodWood. По подрубрикам', current_rubric_for_find=current_rubric_for_find)
        context = dict(list(context.items()) + list(send_to_mixin.items()))
        return context

    def get_queryset(self):
        return Adv.objects.filter(subrubric=self.kwargs['subrubric'], is_active=True)

class OneAdv(DataMixin,DetailView):
    model = Adv
    template_name = 'all_adv/adv.html'
    pk_url_kwarg = 'adv_id'
    context_object_name = 'adv'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        send_to_mixin = self.get_user_context(title='GoodWood. Объявление')
        context = dict(list(context.items()) + list(send_to_mixin.items()))
        return context


def  add_adv(request):
    if request.method == 'POST':
        form_common = AddAdvCommon(request.POST,request.FILES)
        form_for_realty = AddAdvRealtyForm(request.POST,request.FILES)
        form_for_car = AddAdvAutoForm(request.POST,request.FILES)
        form_for_meetting = AddAdvMeettingForm(request.POST,request.FILES)
        form_for_job = AddAdvJobForm(request.POST,request.FILES)
        if form_common.is_valid():
            form_common.save()
            return render(request, 'all_adv/success_page.html')

        elif form_for_realty.is_valid():
            form_for_realty.save()
            return render(request, 'all_adv/success_page.html')

        elif form_for_car.is_valid():
            form_for_car.save()
            return render(request, 'all_adv/success_page.html')

        elif form_for_meetting.is_valid():
            form_for_meetting.save()
            return render(request, 'all_adv/success_page.html')

        elif form_for_job.is_valid():
            form_for_job.save()
            return render(request, 'all_adv/success_page.html')

    else:
        form_common = AddAdvCommon()
        form_for_realty = AddAdvRealtyForm()
        form_for_car = AddAdvAutoForm()
        form_for_meetting = AddAdvMeettingForm()
        form_for_job = AddAdvJobForm()

    rubrics = Rubric.objects.all()
    context = {
        'form_common': form_common,
        'form_for_realty': form_for_realty,
        'form_for_car': form_for_car,
        'form_for_meetting': form_for_meetting,
        'form_for_job': form_for_job,
        'rubrics':rubrics,
        'menu': menu,
        'page': 'add',
        'title': 'GoodWood. Добавить объявление'
    }
    return render(request,'all_adv/create_form.html',context)

def interesting(requests):
    return HttpResponse('Вкладка: Интересно')

def contact(requests):
    return HttpResponse('Вкладка: Контакты')

def login(requests):
    return HttpResponse('Вкладка: Вход')
def register(requests):
    return HttpResponse('Вкладка: Регистрация')
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def find_by_filter(requests):
    if requests.method == 'GET':
        print(requests.GET)
        return HttpResponseRedirect('/all_adv/')
    else:
        print('Не прошло')
        return render(requests,'all_advs.html')
