from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('blog-page/', views.blog, name='blogpost'),
    path('blog-slug/', views.blog_details, name='blog_details'),
  
    
]
