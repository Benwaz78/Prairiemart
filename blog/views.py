from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from blog.models import *

from django.conf import settings
from django.contrib import messages
from django.db.models import Count, Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog(request):
    count_post = Post.objects.filter().count()    
    most_recent = Post.objects.order_by('created')[:4]
    posts = Post.objects.order_by('-created')
    paginated_filter = Paginator(posts, 6)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filter.get_page(page_number)

    context = {
        'person_page_obj': posts, 
        'most_recent': most_recent,
        'post':posts,
        'counts': count_post,
    }
    context['person_page_obj'] = person_page_obj  
    person_page_obj = paginated_filter.get_page(page_number)
    
    return render(request, 'prairiemartapp/blog.html', context)

def blog_details(request):
    return render(request, 'prairiemartapp/blog_post.html')
 