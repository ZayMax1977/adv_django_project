from django.forms import ModelForm
from all_adv.models import Adv


class AdvForm(ModelForm):
    help_texts = "выбор категории"
    class Meta:
        model = Adv
        fields = ('title','content','price','rubric')

