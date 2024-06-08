from django.contrib import admin
from.models import Pet





# # Register your models here.
# @admin.register(Pet)
# class PetAdmin(admin.ModelAdmin):
#     list_display=('id','Petname','species','Breed','Age','price','Gender','Description')
#     search_fields=('Petname','Age')
    



admin.site.register(Pet)

    
