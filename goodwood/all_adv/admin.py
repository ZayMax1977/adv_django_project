from django.contrib import admin

# Register your models here.
from all_adv.models import Adv, Rubric


class AdvAdmin(admin.ModelAdmin):
    list_display = ('title','rubric','content','price','published')
    list_display_links = ('title', 'content')
    search_fields = ('title','price','rubric')
class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Adv,AdvAdmin)
admin.site.register(Rubric,RubricAdmin)