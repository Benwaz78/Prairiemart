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
      auth_views.PasswordResetView.as_view(template_name='auth/forget-password.html', 
       email_template_name='auth/password-reset-email.html', 
       extra_context={'reset':CustomPasswordResetForm},
      success_url = reverse_lazy('dashboard:password_reset_done')), name='password_reset'
   ),
     path(
        'password-reset-done/',
        auth_views.PasswordResetDoneView.as_view(template_name='auth/password-reset-done.html'),
        name='password_reset_done'
     ),

     path(
        'password-reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='auth/password-confirm-form.html',
        extra_context={'con':CustomSetPasswordForm},
        success_url = reverse_lazy('dashboard:password_reset_complete'), form_class=CustomSetPasswordForm), name='password_reset_confirm'
     ),
      path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='auth/password-reset-complete.html'), 
        name='password_reset_complete'
     ),
   
    path('dashboard-page/', views.admin_dashboard, name='admin_dashboard'),
    path('change-password/', views.change_password, name='change_password'),
    path('add-admin/', views.add_admin, name='add_admin'),

]