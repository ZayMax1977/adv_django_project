from django import template
from all_adv.models import *


register = template.Library()

@register.simple_tag()
def get_rubrics():
    return Rubric.objects.all()

@register.simple_tag()
def get_advs():
    return Adv.objects.all()