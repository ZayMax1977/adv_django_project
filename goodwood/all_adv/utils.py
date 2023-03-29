from all_adv.templates.all_adv.rubrics import SUB_RUBRICS_ARR, RUBRIC_ARR

menu = [
    {'title': 'Главная','page_url':'index'},
    {'title': 'Объявления', 'page_url': 'all_advs'},
    {'title': 'Подать', 'page_url': 'add'},
    {'title': 'Интересно', 'page_url': 'interesting'},
    {'title': 'Контакты', 'page_url': 'contact'},
    # {'title': 'Регистрация', 'page_url': 'register'},
    # {'title': 'Вход', 'page_url': 'login'},

]

class DataMixin:
    # надо поставить цифру 12
    paginate_by = 3

    def get_user_context(self,**kwargs):
        context = kwargs
        context['menu'] = menu
        # для показа активности страницы затемнением кнопки
        # использовал в меню base.html приложения all_adv
        context['SUB_RUBRICS_ARR'] = SUB_RUBRICS_ARR
        context['RUBRIC_ARR'] = RUBRIC_ARR
        return  context
