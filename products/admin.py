from django.contrib import admin
from products.models import *
from django.contrib.auth.admin import UserAdmin



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cat_name',)}
    list_display = [
        'cat_name',
        'slug',
        'created',
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brand_name',)}
    list_display = [
        'brand_name',
        'slug',
        'created',
    ]

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('size',)}
    list_display = [
        'size',
        'slug',
        'created',
    ]


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('prod_name',)}
    list_display = [
        'prod_name',
        'slug',
        'price',
        'created',
    ]
