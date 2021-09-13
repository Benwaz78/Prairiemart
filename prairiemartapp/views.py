from django.shortcuts import render
from django.http import HttpResponse
from prairiemartapp.models import *
from products.models import Category,Products,Brand
from django.shortcuts import render, redirect,get_object_or_404


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(in_stock=True)
    brand = Brand.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=category)
        brand = get_object_or_404(Brand, slug=category_slug)
    return render(request, 'prairiemartapp//index.html',{'category': category, 'categories': categories, 'products': products, 'brand':brand})

def about(request):
    return render(request, 'prairiemartapp/about.html')

def blog(request):
    return render(request, 'prairiemartapp/blog.html')

def blog_details(request):
    return render(request, 'prairiemartapp/blog_post.html')


def contact(request):
    return render(request, 'prairiemartapp/contact.html')

def checkout(request):
    return render(request, 'prairiemartapp/checkout.html')

def product(request):
    return render(request, 'prairiemartapp/product.html')

def order(request):
    return render(request, 'prairiemartapp/order.html')

def compare(request):
    return render(request, 'prairiemartapp/compare.html')

def wishlist(request):
    return render(request, 'prairiemartapp/wishlist.html')

def category_grid(request):
    return render(request, 'prairiemartapp/category_grid.html')

def category_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(in_stock=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=category)
    
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'prairiemartapp/category_list.html',context)

def login(request):
    return render(request, 'prairiemartapp/login.html')

def dashboard(request):
    return render(request, 'prairiemartapp/dashboard.html')

def show_cat(request):
    return render(request, 'prairiemartapp/show-cat.html')



