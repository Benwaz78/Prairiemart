from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('add-post', views.PostFormView.as_view(), name='add_post'),
    path('list-posts/', views.ListPosts.as_view(), name='list_posts'),
    path('edit-post/<int:pk>/', views.UpdatePost.as_view(), name='edit_post'),
    path('delete-post/<int:pk>/', views.DeletePost.as_view(), name='delete_post'),
    path('single-post/<int:pk>/', views.SinglePost.as_view(), name='single_post'),
]