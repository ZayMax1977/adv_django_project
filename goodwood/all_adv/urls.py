from django.urls import path

from all_adv.views import index, by_rubric, AdvCreateView

urlpatterns = [
    path('', index, name='index'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/',AdvCreateView.as_view(), name ='add')

]