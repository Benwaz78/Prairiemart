from dashboard import views
from django.urls import path
from django.contrib.auth import views as auth_views
from dashboard.forms import  CustomPasswordResetForm, CustomSetPasswordForm
from django.urls import reverse_lazy

app_name = 'dashboard'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout-page/', views.logout_user, name='logout_user'),
    path(
      'reset-password/',
      auth_views.PasswordResetView.as_view(template_name='prairiemartapp/forget-password.html', 
       email_template_name='auth/password-reset-email.html', 
       extra_context={'reset':CustomPasswordResetForm},
      success_url = reverse_lazy('dashboard:password_reset_done')), name='password_reset'
   ),
     path(
        'password-reset-done/',
        auth_views.PasswordResetDoneView.as_view(template_name='prairiemartapp/password-reset-done.html'),
        name='password_reset_done'
     ),

     path(
        'password-reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='prairiemartapp/password-confirm-form.html',
        success_url = reverse_lazy('dashboard:password_reset_complete'), form_class=CustomSetPasswordForm), name='password_reset_confirm'
     ),
      path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='prairiemartapp/password-reset-complete.html'), 
        name='password_reset_complete'
     ),
   
    path('dashboard-page/', views.admin_dashboard, name='admin_dashboard'),
    path('change-password/', views.change_password, name='change_password'),
    path('add-admin/', views.add_admin, name='add_admin'),
    path('edit-form/', views.edit_form, name='edit_form'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('edit-vendor-profile/', views.edit_vendor_profile_form, name='edit_vendor_profile_form'),
    path('register-vendor/', views.AddVendorView.as_view(), name='add_vendor'),
    path('register-customer/', views.RegisterCustomerView.as_view(), name='reg_customer'),
    path('list-users/', views.ListUsers.as_view(), name='list_users'),
    path('single-user/<int:pk>/', views.SingleUser.as_view(), name='single_user'),
    path('delete-user/<int:pk>/', views.DeleteUser.as_view(), name='delete_user'),
    path('update-user/<int:pk>/', views.UpdateUser.as_view(), name='update_user'),
    path('activate-user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate-user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),

]