from django.urls import path

from .views import by_rubric, AdvCreateView, all_advs, adv, by_subrubric

urlpatterns = [
    path('', all_advs, name='all_advs'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('adv/<int:adv_id>/', adv, name='adv'),

    path('<str:subrubric>/', by_subrubric, name='by_subrubric'),

    path('add/', AdvCreateView.as_view(), name='add')

]