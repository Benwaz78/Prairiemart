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


# post views
class PostFormView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = '/dashboard/'
    model = Post
    template_name = 'dashboard/post/add-edit-post.html'
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
    template_name = 'dashboard/post/add-edit-post.html/'
    success_url = reverse_lazy('blog:edit_post')
    success_message = 'Post edited successfully'
    form_class = PostForm


class ListPosts(LoginRequiredMixin, ListView):
    login_url = '/dashboard/'
    model = Post
    paginate_by = 4
    template_name =  'dashboard/post/list-post.html'
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


class PostCategoryFormView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/dashboard/'
    model = Post
    paginate_by = 4
    template_name = 'dashboard/category-post/add-edit-category-post.html'
    success_url = reverse_lazy('blog:post_cat')
    success_message = 'Category added successfully'
    form_class = PostCategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_post'] = Category.objects.all()
        return context


    def form_valid(self, cat):
        randomize = random.randint(0, 999999999999)
        concate = f'{randomize}-{cat.instance.cat_name}'
        cat.instance.slug = slugify(concate)
        return super().form_valid(cat)

class UpdatePostCategory(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    model = Category
    success_url = reverse_lazy('blog:edit_cat')
    success_message = 'Category edited successfully'
    form_class = PostCategoryForm
    template_name = 'dashboard/category-post/add-edit-category-post.html'
    
    def get_success_url(self):
        return reverse('blog:edit_cat', kwargs={'pk' : self.object.pk})

class DeleteCategory(LoginRequiredMixin, DeleteView):
    login_url = '/dashboard/'
    model = Category
    success_url = reverse_lazy('blog:post_cat')

# Product Category views ends here

