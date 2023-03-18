from django.forms import ModelForm
from all_adv.models import Adv


class AdvForm(ModelForm):
    help_texts = "выбор категории"

    class Meta:
        model = Adv

        fields = ['title',
                  'transaction',
                  'region',
                  'city',
                  'district_city',
                  'user_name',
                  'phone_number',
                  'content',
                  'price',
                  'rubric',
                  'subrubric',


                  'street',
                  'floors',
                  'floor',
                  'rooms',
                  'square_rooms',
                  'square_land',
                  'law_status',
                  'ower',

                  'car_mark',
                  'car_model',
                  "car_year",
                   'car_fuel',
                  'car_color',
                  "car_body",
                  "car_actuator",
                  "car_transmission",
                  "car_run",
                  "car_engine_capacity",

                  "who",
                  "whom",
                  'your_age',
                  "intention_age",
                  "intention",

                  "salary",
                  "mode"

                  ]


