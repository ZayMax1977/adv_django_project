from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView

from posts.models import PostList, Category

menu = [
    {'title': 'Главная','page_url':'index'},
    {'title': 'Объявления', 'page_url': 'all_advs'},
    {'title': 'Подать', 'page_url': 'add'},
    {'title': 'Контакты', 'page_url': 'contact'},
    {'title': 'Статьи','page_url':'posts'}

]

class PostListView(ListView):
    model = PostList
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'posts'
        context['menu'] = menu
        context['category'] = Category.objects.all()
        return context

    def get_queryset(self):
        return PostList.objects.all()

