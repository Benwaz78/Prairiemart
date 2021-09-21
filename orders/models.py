from decimal import Decimal

from django.conf import settings
from django.db import models

from products.models import Products


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    full_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Order'
    
    def __str__(self):
        return f'{self.user.username} created this order @ this time {self.created}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Products,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'This Order Item Id {self.id} is this product {self.product.title}'

    def get_cost(self):
        return self.product.price * self.quantity