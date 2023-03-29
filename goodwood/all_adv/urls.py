from django.urls import path
from django.views.decorators.cache import cache_page
from .views import find_by_filter, interesting, add_adv, AllAdvs, ByRubric, BySubRubric, OneAdv, RegisterUser, LoginUser, \
    logout_user, ContactFormOur

urlpatterns = [
    path('', AllAdvs.as_view(), name='all_advs'),
    path('add/', add_adv, name='add'),

    path('interesting/', interesting, name='interesting'),
    path('contact/',ContactFormOur.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),

    path('find_by_filter/', find_by_filter, name='find_by_filter'),

    path('<int:rubric_id>/', ByRubric.as_view(), name='by_rubric'),
    path('<str:subrubric>/', BySubRubric.as_view(), name='by_subrubric'),

    path('adv/<int:adv_id>/', OneAdv.as_view(), name='adv'),

]

