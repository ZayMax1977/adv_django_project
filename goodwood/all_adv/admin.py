from django.contrib import admin

# Register your models here.
from all_adv.models import Adv, Rubric, Transaction, Region, CarMark, LawStatus, Subject, CarFuel, CarTransmission, CarActuator, CarBody, \
    Intention


class AdvAdmin(admin.ModelAdmin):
    list_display = ('id','is_active','title','rubric',"subrubric",'transaction','law_status','region','city','content','price','user_name',
    'phone_number','street',
                    'floors','floor','rooms','square_rooms','square_land','car_mark','car_model','car_color','car_year','published')
    list_display_links = ('title', 'content')
    search_fields = ('is_active','title','price','rubric','subrubric','transaction','region','city')

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

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

class LawStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class CarFuelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class CarTransmissionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class CarActuatorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class CarBodyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class IntentionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Adv,AdvAdmin)
admin.site.register(Rubric,RubricAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(LawStatus,LawStatusAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(CarMark,CarMarkAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(CarFuel,CarFuelAdmin)
admin.site.register(CarActuator,CarActuatorAdmin)
admin.site.register(CarBody,CarBodyAdmin)
admin.site.register(Intention,IntentionAdmin)



