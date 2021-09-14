from django.shortcuts import render, redirect
from django.http import HttpResponse
from prairiemartapp.models import *
from dashboard.forms import *
from prairiemartapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from products.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from products.forms import *


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





def index(request):
    return render(request, 'prairiemartapp/index.html')

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
    products = Products.objects.filter()
    brand = Brand.objects.order_by('created')
    size = Size.objects.order_by('created')
    paginated_filter = Paginator(products, 16)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filter.get_page(page_number)

    context = {
        'brands':brand,
        'size':size,
        'person_page_obj': products,
       
    }

    context['person_page_obj'] = person_page_obj  
    person_page_obj = paginated_filter.get_page(page_number)
    return render(request, 'prairiemartapp/category_grid.html', context)

def category_list(request):
    return render(request, 'prairiemartapp/category_list.html')


def cutomer_dashboard(request):
    return render(request, 'prairiemartapp/dashboard.html')

def show_cat(request):
    return render(request, 'prairiemartapp/show-cat.html')

def filtersearch(request):
    products = Products.objects.filter()
    paginated_filter = Paginator(products, 16)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filter.get_page(page_number)
    if request.method == 'GET':
        query_form = FilterForm(request.GET)
        if query_form.is_valid():
            print('Correct')
            prod_name = query_form.cleaned_data.get('prod_name')
            category = query_form.cleaned_data.get('category')
            query = Products.objects.filter(prod_name=prod_name, category=category )
            context = {
            'person_page_obj': products,
            'q': query,
        }
            context['person_page_obj'] = person_page_obj  
            person_page_obj = paginated_filter.get_page(page_number)
            return render(request, 'prairiemartapp/search_results.html', context)
        else:
            print('Not found')
    return render(request, 'prairiemartapp/search_results2.html')