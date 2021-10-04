from django.contrib import admin
from .models import Products
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','pname','price','pqty']

admin.site.register(Products,ProductAdmin)