from django.forms import models
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from products.models import *
from products.forms import *
from basket.forms import CartAddProductForm
from basket.basket import Basket


from django.urls import reverse_lazy
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import(
    ListView, DeleteView, 
    DetailView, CreateView,
    UpdateView, View, TemplateView
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

# Brand views Starts Here
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

# Brand views ends here

# Size views starts here
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

# Size views ends here

# Product Category views starts here
class ProductCategoryFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/dashboard/'
    model = Products
    paginate_by = 4
    template_name = 'dashboard/category/add-edit-category.html'
    success_url = reverse_lazy('products:prod_cat')
    success_message = 'Category added successfully'
    form_class = ProductCategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_cat'] = Category.objects.order_by('-created')
        return context


    def form_valid(self, form):
        randomize = random.randint(0, 999999999999)
        concate = f'{randomize}-{form.instance.cat_name}'
        form.instance.slug = slugify(concate)
        return super().form_valid(form)


class UpdateProductCategory(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    model = Category
    success_url = reverse_lazy('backend:edit_cat')
    success_message = 'Category edited successfully'
    form_class = ProductCategoryForm
    template_name = 'dashboard/category/add-edit-category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_cat'] = Category.objects.order_by('-created')
        return context

class DeleteCategory(LoginRequiredMixin, DeleteView):
    login_url = '/dashboard/'
    model = Category
    success_url = reverse_lazy('products:prod_cat')

# Product Category views ends here

class UpdateProductCategory(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    model = Category
    success_url = reverse_lazy('backend:edit_cat')
    success_message = 'Category edited successfully'
    form_class = ProductCategoryForm
    template_name = 'dashboard/category/add-edit-category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_cat'] = Category.objects.order_by('-created')
        return context


def category_grid(request, category_slug=None):
    basket = Basket(request)
    cart_product_form = CartAddProductForm()
    object_list = Products.objects.all()
    products = Products.objects.filter(in_stock=True)
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=category)
        paginator = Paginator(object_list, 1)  # number of products that will appear in each page
        page = request.GET.get('page')
        try:
            prod = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer deliver the first page
            prod = paginator.page(1)
        except EmptyPage:
        # If page is out of range deliver last page of results
            prod = paginator.page(paginator.num_pages)
    
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form,
        'basket':basket,
        'page':page,
        'prod':prod
    }

    return render(request, 'prairiemartapp/products-by-category-grid.html',context)

def product_detail(request, id, slug, category_slug=None):
    basket = Basket(request)
    product = get_object_or_404(Products, id=id, slug=slug, in_stock=True)
    cart_product_form = CartAddProductForm()
    products = Products.objects.filter(in_stock=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=category)

    context = {
        'product': product,
        'products': products,
        'cart_product_form': cart_product_form,
        'basket': basket
    }
    return render(request, 'prairiemartapp/product.html', context)

def category_list(request):
    return render(request, 'prairiemartapp/category-list.html')

# class ProductsByCategoryGrid(ListView):
#     template_name = 'prairiemartapp/products-by-category-grid.html'
#     context_object_name = 'product_category'

#     def get_queryset(self):
#         self.category = get_object_or_404(Category, cat_name=self.kwargs['category'])
#         return Products.objects.filter(category=self.category)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category_name'] = self.category.cat_name
#         return context

 
class ProductsByBrandView(ListView):
    template_name = 'prairiemartapp/products-by-brand-grid.html'
    context_object_name = 'product_brand'

    def get_queryset(self):
        self.brand = get_object_or_404(Brand, brand_name=self.kwargs['brand'])
        return Products.objects.filter(brand=self.brand)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_brand_name'] = self.brand.brand_name
        return context
