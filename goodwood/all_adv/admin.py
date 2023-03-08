from django.contrib import admin

# Register your models here.
from all_adv.models import Adv, Rubric, Transaction,  Region, CarMark


class AdvAdmin(admin.ModelAdmin):
    list_display = ('id','is_active','title','rubric',"subrubric",'transaction','region','city','content','price','user_name','phone_number','street',
                    'floors','floor','rooms','square_rooms','square_land','car_mark','car_model','car_color','car_year','published')
    list_display_links = ('title', 'content')
    search_fields = ('is_active','title','price','rubric','subrubric','transaction','region','city')

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

# class SubRubricAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     list_display_links = ('name',)
#     search_fields = ('name',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Adv,AdvAdmin)
admin.site.register(Rubric,RubricAdmin)
admin.site.register(Transaction,TransactionAdmin)
# admin.site.register(SubRubric,SubRubricAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(CarMark,CarMarkAdmin)