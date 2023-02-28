from django.urls import path

from all_adv.views import index

urlpatterns = [
    path('', index),

]