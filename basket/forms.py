from django import forms
from .import models
from django.core import validators

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    









