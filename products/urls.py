from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductFormView.as_view(), name='add_product'),
    path('list-products/', views.ListProducts.as_view(), name='list_products'),
    path('edit-product/<int:pk>/', views.UpdateProduct.as_view(), name='edit_product'),
    path('delete-product/<int:pk>/', views.DeleteProduct.as_view(), name='delete_product'),
    path('single-product/<int:pk>/', views.SingleProduct.as_view(), name='single_product'),
    
]
