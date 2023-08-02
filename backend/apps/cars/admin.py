from django.contrib import admin

from .models import CarModel


# Register your models here.

@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'brand', 'year']
