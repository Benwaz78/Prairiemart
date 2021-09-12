from django.db import models

# Create your models here.
from django.utils import timezone
from dashboard.managers import CustomAccountManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    profile = models.ImageField(null=True, blank=True, upload_to='uploads/')
    

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name

    def get_profile(self):
        if self.profile:
            return self.profile.url
        else:
            return '/static/dashboard/images/faces/avatar.png'