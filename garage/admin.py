from django.contrib import admin
from .models import *


@admin.register(Manufacturers)
class AdminManufacturers(admin.ModelAdmin):
    list_display = ['title']

@admin.register(CarModels)
class AdminCarModels(admin.ModelAdmin):
    list_display = ['title', 'manufacturer']

@admin.register(Mechanics)
class AdminMechanics(admin.ModelAdmin):
    list_display = ['first_name', 'patronymic', 'second_name', 'experience']

@admin.register(Owners)
class AdminOwners(admin.ModelAdmin):
    list_display = ['first_name', 'patronymic', 'second_name', 'first_application']
    readonly_fields = ['first_application']

@admin.register(Cars)
class AdminCars(admin.ModelAdmin):
    list_display = [
        'manufacturer', 
        'car_model',
        'color',
        'owner',
        'gov_number',
        'year',
        'ser_sts',
        'num_sts',
        'date_of_application',
        'date_of_issue',
        'photo',
        'scan_sts',
        'mechanic',
        ]
    
@admin.register(PriceList)
class AdminPriceList(admin.ModelAdmin):
    list_display = ['type_of_repair', 'price']