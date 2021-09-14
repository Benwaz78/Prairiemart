from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductFormView.as_view(), name='add_product'),
    path('list-products/', views.ListProducts.as_view(), name='list_products'),
    path('edit-product/<int:pk>/', views.UpdateProduct.as_view(), name='edit_product'),
    path('delete-product/<int:pk>/', views.DeleteProduct.as_view(), name='delete_product'),
    path('single-product/<int:pk>/', views.SingleProduct.as_view(), name='single_product'),
    path('add-brand', views.BrandFormView.as_view(), name='add_brand'),
    path('list-brands/', views.ListBrands.as_view(), name='list_brands'),
    path('edit-brand/<int:pk>/', views.UpdateBrand.as_view(), name='edit_brand'),
    path('delete-brand/<int:pk>/', views.DeleteBrand.as_view(), name='delete_brand'),
    path('single-brand/<int:pk>/', views.SingleBrand.as_view(), name='single_brand'),
    path('add-size/', views.SizeFormView.as_view(), name='add_size'),
    path('list-sizes/', views.ListSizes.as_view(), name='list_sizes'),
    path('edit-size/<int:pk>/', views.UpdateSize.as_view(), name='edit_size'),
    path('delete-size/<int:pk>/', views.DeleteSize.as_view(), name='delete_size'),
    path('single-size/<int:pk>/', views.SingleSize.as_view(), name='single_size'),
    path('product-category/', views.ProductCategoryFormView.as_view(), name='prod_cat'),
    path('edit-product-category/<int:pk>/', views.UpdateProductCategory.as_view(), name='edit_cat'),
    path('del-product-category/<int:pk>/', views.DeleteCategory.as_view(), name='del_cat'),
    path('category-grid-page/', views.category_grid, name='category_grid'),
    path('category-list-page/', views.category_list, name='category_list'),
    path('category/<category>/', views.ProductsByCategoryGrid.as_view(), name='prod_by_category_grid'),
    path('brand/<brand>/', views.ProductsByBrandView.as_view(), name='prod_by_brand'),

]
