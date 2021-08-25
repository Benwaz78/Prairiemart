from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'prairiemartapp//index.html')

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

def login(request):
    return render(request, 'prairiemartapp/login.html')
