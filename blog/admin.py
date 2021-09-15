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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = [
        'cat_name',
    
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


