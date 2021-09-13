from cProfile import label
from unicodedata import category
from django import forms
from dashboard.models import *
from products.models import *
from django.core import validators



class ProductForm(forms.ModelForm):
    prod_name = forms.CharField(label='Product Name*', widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Product Name'}
    ))
    category = forms.ModelChoiceField(
        label='Product Category*',
		queryset=Category.objects.all(), 
		widget=forms.Select(attrs={'class': 'form-control'}),
		empty_label='Select Product Category'
		)

    brand = forms.ModelChoiceField(
        required=False,
		queryset=Brand.objects.all(), 
		widget=forms.Select(attrs={'class': 'form-control'}),
		empty_label='Select Brand'
		)

    size = forms.ModelChoiceField(
        required=False,
        queryset=Size.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Select Size'
    )
    price = forms.DecimalField(
        label='Prize*',
        widget=forms.NumberInput(
            attrs={'class':'form-control', 'placeholder':'Prize*'}
        )
    )

    in_stock = forms.BooleanField(
        required=False
    )
    image1 = forms.ImageField(
        label='Product Image 1*',
        widget=forms.ClearableFileInput(
            attrs={'class':'form-control',}
        )
    )
    image2 = forms.ImageField(
        label='Product Image 2*',
        widget=forms.ClearableFileInput(
            attrs={'class':'form-control',}
        )
    )
    image3 = forms.ImageField(
        label='Product Image 3*',
        widget=forms.ClearableFileInput(
            attrs={'class':'form-control',}
        )
    )
    description = forms.CharField(
        label='Description*',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
            }
        )
    )

    class Meta():
        model = Products
        exclude = ('created_by', 'created', 'updated', 'slug', 'objects', 'products')



class BrandForm(forms.ModelForm):
    brand_name = forms.CharField(
        label='Brand Name',
        widget=forms.TextInput(
            attrs={'class':'form-control'}))
    brand_img = forms.ImageField(
        label= 'Brand Image',
        widget= forms.ClearableFileInput(
            attrs={'class':'form-control'}
        )
    )

    class Meta():
        model = Brand
        exclude = ('slug','created')


class SizeForm(forms.ModelForm):
    size = forms.CharField(
        label ='Size',
        widget =forms.TextInput(
            attrs ={'class':'form-control'}
        )
    )
 

    class Meta():
        model = Size
        exclude = ('slug','created')