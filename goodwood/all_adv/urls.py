from django.urls import path

from .views import by_rubric, AdvCreateView, all_advs

urlpatterns = [
    path('', all_advs, name='all_advs'),

    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', AdvCreateView.as_view(), name='add')

]