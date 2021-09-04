from django.db import models
from django.utils import timezone
from prairiemartapp.managers import CustomAccountManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    cat_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.cat_name

    def save(self, *args, **kwargs):
        self.cat_name = self.cat_name.capitalize()
        return super().save(*args, **kwargs)

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    

