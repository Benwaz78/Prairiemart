from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('blog-page/', views.blog, name='blogpost'),
  
    path('blog-single-post/<int:pk>/', views.blog_post, name='blog_single_post'),
  
    
]
