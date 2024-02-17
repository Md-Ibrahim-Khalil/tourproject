from django.contrib import admin
from . models import Agency, Tour



# Register your models here.
@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ['id','name','nid_number','phone_number']
    
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'package_name', 'package_price', 'confirmed']
    
    
