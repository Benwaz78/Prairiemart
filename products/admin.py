from django.contrib import admin
from products.models import *
from django.contrib.auth.admin import UserAdmin



admin.site.register(Category)

admin.site.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = [
        'title',
        'slug',
        'price',
        'created',
    ]
