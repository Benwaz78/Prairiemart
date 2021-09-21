from django.urls import path
from django.conf.urls import url

from basket import views

app_name = 'basket'

urlpatterns = [
    url(r'^basket_summary/$', views.basket_summary, name='basket_summary'),
    url(r'^add/(?P<product_id>\d+)/$',views.basket_add, name='basket_add'),
    url(r'^delete/(?P<product_id>\d+)/$', views.basket_delete, name='basket_delete'),
    # path('update/', views.basket_update, name='basket_update'),
]
