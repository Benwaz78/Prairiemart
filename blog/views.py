from django.forms import models
from django.shortcuts import render
from blog.models import *
from blog.forms import *

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

# class BlogSinglePost(DetailView):
#     model = Post
#     form_class = CommentForm
#     template_name = 'prairiemartapp/blog_post.html'
#     context_object_name = 'blog_single_post'
 
def blog_post(request, pk):
    most_recent = Post.objects.order_by('created')[:6]
    most_recent_comment = Comment.objects.filter(post=pk).order_by('-created_on')[:4]
    single_post = get_object_or_404(Post,  pk=pk)
    comments = Comment.objects.filter(post=pk).order_by('-created_on')
 
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = single_post
            comment.save()
            return redirect('prairiemartapp:blog_single_post', pk=single_post.pk)

    else:
        form = CommentForm()     
    context ={
        'comm':comments, 
        'form':form,
        'single':single_post, 
        'most_recent':most_recent,
        'sipst':single_post,
        'most_recent_comment':most_recent_comment,
    }
    return render(request, 'prairiemartapp/blog_post.html', context)

# post views
class PostFormView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = '/dashboard/'
    model = Post
    template_name = '/dashboard/post/add-edit-post.html'
    success_url = reverse_lazy('blog:add_post')
    success_message = 'Post added successfully'
    form_class = PostForm

    def form_valid(self, post):
        post.instance.user = self.request.user
        randomize = random.randint(0, 999999999999)
        concate = f'{randomize}-{post.instance.pst_title}'
        post.instance.slug = slugify(concate)
        return super().form_valid(post)


class UpdatePost(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = '/dashboard/'
    model = Post
    template_name = '/dashboard/post/add-edit-post.html/'
    success_url = reverse_lazy('backend:add_meeting')
    success_message = 'Post edited successfully'
    form_class = PostForm


class ListPosts(LoginRequiredMixin, ListView):
    login_url = '/dashboard/'
    model = Post
    paginate_by = 4
    template_name =  'dashboard/posts/list-posts.html'
    context_object_name = 'list_posts'

class DeletePost(LoginRequiredMixin, DeleteView):
    login_url = '/dashboard/'
    model = Post
    success_url = reverse_lazy('blog:list_posts')

class SinglePost(LoginRequiredMixin, DetailView):
    login_url = '/dashboard/'
    model = Post
    template_name = 'dashboard/posts/single-post.html'
    context_object_name = 'single_post'


