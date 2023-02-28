from django.http import HttpResponse
from django.shortcuts import render

from all_adv.models import Adv


def index(requests):
    advs = Adv.objects.all()


    return render(requests,'all_adv/index.html',{"advs":advs})

