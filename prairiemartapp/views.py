from django.shortcuts import render, redirect
from django.http import HttpResponse
from prairiemartapp.models import *
from products.models import Category,Products,Brand
from django.shortcuts import render, redirect,get_object_or_404
from dashboard.forms import *
from prairiemartapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from basket.basket import Basket



@login_required(login_url='/dashboard/')                                                                                                                                                                                                                                                                                                                                                                                                                            
def change_password(request):
    if request.method == 'POST':
        change_password = ChangePasswordForm(data=request.POST, user=request.user)
        if change_password.is_valid():
            change_password.save()
            update_session_auth_hash(request, change_password.user)
            messages.success(request, 'Password Changed Successfully')
    else:
        change_password = ChangePasswordForm(user=request.user)
    return render(request, 'prairiemartapp/change-password.html', {'change_pass':change_password})


@login_required(login_url='/dashboard/')
def view_profile(request):
    return render(request, 'prairiemartapp/view-profile.html', {'view':request.user})

@login_required(login_url='/dashboard/')
def edit_form(request):
    if request.method == 'POST':
        edit_form = EditCustomerProfileForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('prairiemartapp:view_profile')
    else:
        edit_form = EditCustomerProfileForm(instance=request.user)
    return render(request, 'prairiemartapp/edit-profile.html', {'edit':edit_form})






def index(request, category_slug=None):
    basket = Basket(request)
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(in_stock=True)
    brand = Brand.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=category)
        brand = get_object_or_404(Brand, slug=category_slug)
    return render(request, 'prairiemartapp//index.html',{'basket':basket, 'category': category, 'categories': categories, 'products': products, 'brand':brand})

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

def category_list(request):
    return render(request, 'prairiemartapp/category_list.html')


def cutomer_dashboard(request):
    return render(request, 'prairiemartapp/dashboard.html')

def show_cat(request):
    return render(request, 'prairiemartapp/show-cat.html')

def login(request):
    return render(request, 'prairiemartapp/login.html')