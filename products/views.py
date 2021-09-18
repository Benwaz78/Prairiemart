from django.forms import models
from django.shortcuts import render, get_object_or_404
from products.models import *
from products.forms import *

from django.urls import reverse_lazy
from django.utils.text import slugify

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import(
    ListView, DeleteView, 
    DetailView, CreateView,
    UpdateView, View, TemplateView,FormView
    )

import random



class ProductFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/dashboard/'
    model = Products
    template_name = 'dashboard/products/add-edit-product.html'
    success_url = reverse_lazy('products:add_product')
    success_message = 'Product added successfully'
    form_class = ProductForm

    def images(self,request):
        files = request.FILES.getlist('image1')
        if form.is_valid():
            for f in files:
                image=ProductForm(
                    image1 = f
                )
                image.save()
            return self.form_valid(form)
        else:
            return self.form_valid(form)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        randomize = random.randint(0, 999999999999)
        concate = f'{randomize}-{form.instance.prod_name}'
        form.instance.slug = slugify(concate)
        return super().form_valid(form)

class UpdateProduct(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    model = Products
    success_url = reverse_lazy('products:edit_product')
    success_message = 'Product edited successfully'
    form_class = ProductForm
    template_name = 'dashboard/products/add-edit-product.html'

    def get_success_url(self):
        return reverse('products:edit_product', kwargs={'pk' : self.object.pk})

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

    def form_valid(self, brand):
        randomize = random.randint(0, 999999999999)
        concate = f'{randomize}-{brand.instance.brand_name}'
        brand.instance.slug = slugify(concate)
        return super().form_valid(brand)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_brands'] = Brand.objects.all()
        return context

class UpdateBrand(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    model = Brand
    success_url = reverse_lazy('products:edit_brand')
    success_message = 'Brand edited successfully'
    form_class = BrandForm
    template_name = 'dashboard/brand/add-edit-brand.html'


    def get_success_url(self):
        return reverse('products:edit_brand', kwargs={'pk' : self.object.pk})




class ListBrands(LoginRequiredMixin, ListView):
    login_url = '/dashboard/'
    model = Brand
    paginate_by = 4
    template_name =  'dashboard/brand/list-brand.html'
    context_object_name = 'list_brands'

class DeleteBrand(LoginRequiredMixin, DeleteView):
    login_url = '/dashboard/'
    model = Brand
    success_url = reverse_lazy('products:list_brands')

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
    def form_valid(self, size):
        randomize = random.randint(0, 999999999999)
        concate = f'{randomize}-{size.instance.size}'
        size.instance.slug = slugify(concate)
        return super().form_valid(size)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_sizes'] = Size.objects.all()
        return context

    


class UpdateSize(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    model = Size
    success_url = reverse_lazy('products:edit_size')
    success_message = 'Size edited successfully'
    form_class = SizeForm
    template_name = 'dashboard/size/add-edit-size.html'

    def get_success_url(self):
        return reverse('products:edit_size', kwargs={'pk' : self.object.pk})

class ListSizes(LoginRequiredMixin, ListView):
    login_url = '/dashboard/'
    model = Size
    paginate_by = 4
    template_name =  'dashboard/size/list-size.html'
    context_object_name = 'list_sizes'

class DeleteSize(LoginRequiredMixin, DeleteView):
    login_url = '/dashboard/'
    model = Size
    success_url = reverse_lazy('products:list_sizes')

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
    success_url = reverse_lazy('products:edit_cat')
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

# class UpdateProductCategory(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     login_url = '/dashboard/'
#     model = Category
#     success_url = reverse_lazy('backend:edit_cat')
#     success_message = 'Category edited successfully'
#     form_class = ProductCategoryForm
#     template_name = 'dashboard/category/add-edit-category.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['list_cat'] = Category.objects.order_by('-created')
#         return context


def category_grid(request):
    return render(request, 'prairiemartapp/category-grid.html')

def category_list(request):
    return render(request, 'prairiemartapp/category-list.html')

class ProductsByCategoryGrid(ListView):
    template_name = 'prairiemartapp/products-by-category-grid.html'
    context_object_name = 'product_category'

    def get_queryset(self):
        self.category = get_object_or_404(Category, cat_name=self.kwargs['category'])
        return Products.objects.filter(category=self.category)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.category.cat_name
        return context

 
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