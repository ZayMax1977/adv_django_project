
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render, get_object_or_404
# from django.urls import reverse_lazy
# from django.utils import inspect
# from django.views.generic import CreateView

# from all_adv.forms import AdvForm
from all_adv.forms import AddAdvRealtyForm, AddAdvAutoForm, AddAdvCommon, AddAdvMeettingForm, AddAdvJobForm
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
    adv = get_object_or_404(Adv,pk=adv_id)
    # adv = Adv.objects.get(pk=adv_id)
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
            # try:
            #     Adv.objects.create(**form_common.cleaned_data)
            #     return render(request, 'all_adv/success_page.html')
            # except:
            #     form_common.add_error(None,'Ошибка добавления поста')

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

# class AdvCreateView(CreateView):
#     template_name = 'all_adv/create_form.html'
#     form_class = AdvForm
#     success_url = reverse_lazy("all_advs")
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         context['menu'] = menu
#         context['page'] = 'add'
#         context['title'] = 'GoodWood. Добавить объявление'
#
#         return context

def interesting(requests):
    return HttpResponse('Вкладка: Интересно')

def contact(requests):
    return HttpResponse('Вкладка: Контакты')

def log(requests):
    return HttpResponse('Вкладка: Вход')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
