from django.urls import path

from .views import by_rubric, all_advs, adv, by_subrubric,  AdvCreateView

urlpatterns = [
    path('', all_advs, name='all_advs'),
    path('add/', AdvCreateView.as_view(), name='add'),

    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('<str:subrubric>/', by_subrubric, name='by_subrubric'),

    path('adv/<int:adv_id>/', adv, name='adv'),




]