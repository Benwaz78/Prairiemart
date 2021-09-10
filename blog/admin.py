from django.contrib import admin
from blog.models import *

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('pst_title',)}
    list_display = [
        'pst_title',
        'slug',
        'pst_image',
        'user',
        'created',
    ]
