from django.contrib import admin
from prairiemartapp.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'user_name', 'first_name', 'last_name')
    list_display = ('email', 'user_name', 'first_name', 'last_name', 'is_staff', 'is_active')
    ordering = ('-start_date',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (
            None,{
                'classes':('wide',),
                'fields' :('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')
            }
        ),
    )


admin.site.register(CustomUser, UserAdminConfig)
admin.site.register(Category)
admin.site.register(Product)