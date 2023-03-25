from django.urls import path

from .views import by_rubric, all_advs, adv, by_subrubric,  find_by_filter, interesting, contact, log, add_adv

urlpatterns = [
    path('', all_advs, name='all_advs'),
    # path('add/', AdvCreateView.as_view(), name='add'),
    path('add/', add_adv, name='add'),

    path('interesting/', interesting, name='interesting'),
    path('contact/',contact, name='contact'),
    path('login/', log, name='log'),

    path('find_by_filter/', find_by_filter, name='find_by_filter'),

    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('<str:subrubric>/', by_subrubric, name='by_subrubric'),

    path('adv/<int:adv_id>/', adv, name='adv'),

]

