from django.forms import ModelForm
from all_adv.models import Adv


class AdvForm(ModelForm):
    help_texts = "выбор категории"

    class Meta:
        model = Adv

        fields = ['title',
                  'rubric',
                  'subrubric',
                  'transaction',
                  'content',
                  'region',
                  'city',
                  'street',
                  'car_mark',
                  'car_model',
                  'car_year',
                  'car_color',
                  'floors',
                  'floor',
                  'rooms',
                  'square_rooms',
                  'square_land',
                  'user_name',
                  'phone_number',
                  'price']


