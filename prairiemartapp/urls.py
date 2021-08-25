from django.urls import path
from prairiemartapp import views

app_name = 'prairiemartapp'

urlpatterns = [
    path('about-page/', views.about, name='about'),
    path('contact-page/', views.contact, name='contact'),
    path('blog-page/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blogpost'),
    path('checkout/', views.checkout, name='checkout'),
    path('product-page/', views.product, name='product'),
    path('order-page/', views.order, name='order'),
    path('compare-page/', views.compare, name='compare'),
    path('wishlist-page/', views.wishlist, name='wishlist'),
    path('category_grid-page/', views.category_grid, name='category_grid'),
    path('category_list-page/', views.category_list, name='category_list'),
    path('login-page/', views.login, name='login'),
    
]
