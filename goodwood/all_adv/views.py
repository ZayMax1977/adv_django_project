from django.http import HttpResponse
from django.shortcuts import render

from all_adv.models import Adv, Rubric


def index(requests):
    advs = Adv.objects.all()
    rubrics = Rubric.objects.all()
    context ={
        "advs": advs,
        "rubrics":rubrics
    }
    return render(requests,'all_adv/index.html',    context)

def by_rubric(requests,rubric_id):
    advs_by_rub = Adv.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'advs_by_rub':advs_by_rub,
        'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(requests,'all_adv/by_rubric.html',context)





