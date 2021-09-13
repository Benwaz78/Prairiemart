from django.forms import models
from django.shortcuts import render
from products.models import *
from products.forms import *

from django.urls import reverse_lazy
from django.utils.text import slugify

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import(
    ListView, DeleteView, 
    DetailView, CreateView,
    UpdateView, View
    )

import random



class ProductFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/dashboard/'
    model = Products
    template_name = 'dashboard/products/add-edit-product.html'
    success_url = reverse_lazy('products:add_product')
    success_message = 'Product added successfully'
    form_class = ProductForm


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        randomize = random.randint(0, 999999999999)
        concate = f'{randomize}-{form.instance.prod_name}'
        form.instance.slug = slugify(concate)
        return super().form_valid(form)

class UpdateProduct(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    model = Products
    success_url = reverse_lazy('backend:add_meeting')
    success_message = 'Product edited successfully'
    form_class = ProductForm
    template_name = 'dashboard/products/add-edit-product.html'

class ListProducts(LoginRequiredMixin, ListView):
    login_url = '/dashboard/'
    model = Products
    paginate_by = 4
    template_name =  'dashboard/products/list-products.html'
    context_object_name = 'list_products'

class DeleteProduct(LoginRequiredMixin, DeleteView):
    login_url = '/dashboard/'
    model = Products
    success_url = reverse_lazy('products:list_products')

class SingleProduct(LoginRequiredMixin, DetailView):
    login_url = '/dashboard/'
    model = Products
    template_name = 'dashboard/products/single-product.html'
    context_object_name = 'single_product'

# Brand views

class BrandFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/dashboard/'
    model = Brand
    template_name = 'dashboard/brand/add-edit-brand.html'
    success_url = reverse_lazy('products:add_brand')
    success_message = 'Brand added successfully'
    form_class = BrandForm


class UpdateBrand(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    model = Brand
    success_url = reverse_lazy('backend:add_meeting')
    success_message = 'Brand edited successfully'
    form_class = BrandForm
    template_name = 'dashboard/brand/add-edit-brand.html'

class ListBrands(LoginRequiredMixin, ListView):
    login_url = '/dashboard/'
    model = Brand
    paginate_by = 4
    template_name =  'dashboard/brand/list-brand.html'
    context_object_name = 'list_brands'

class DeleteBrand(LoginRequiredMixin, DeleteView):
    login_url = '/dashboard/'
    model = Brand
    success_url = reverse_lazy('products:list_brand')

class SingleBrand(LoginRequiredMixin, DetailView):
    login_url = '/dashboard/'
    model = Brand
    template_name = 'dashboard/brand/single-brand.html'
    context_object_name = 'single_product'



# Size views

class SizeFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/dashboard/'
    model = Size
    template_name = 'dashboard/size/add-edit-size.html'
    success_url = reverse_lazy('products:add_size')
    success_message = 'Size added successfully'
    form_class = SizeForm


class UpdateSize(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    model = Size
    success_url = reverse_lazy('backend:add_meeting')
    success_message = 'Size edited successfully'
    form_class = SizeForm
    template_name = 'dashboard/size/add-edit-size.html'

class ListSizes(LoginRequiredMixin, ListView):
    login_url = '/dashboard/'
    model = Size
    paginate_by = 4
    template_name =  'dashboard/size/list-size.html'
    context_object_name = 'list_sizes'

class DeleteSize(LoginRequiredMixin, DeleteView):
    login_url = '/dashboard/'
    model = Size
    success_url = reverse_lazy('products:list_size')

class SingleSize(LoginRequiredMixin, DetailView):
    login_url = '/dashboard/'
    model = Size
    template_name = 'dashboard/size/single-size.html'
    context_object_name = 'single_size'



