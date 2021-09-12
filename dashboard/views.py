from django.shortcuts import render, redirect
from dashboard.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:admin_dashboard')
        else:
            messages.error(request, 'Email and Password do not match')
    return render(request, 'auth/login.html')


@login_required(login_url='/dashboard/')
def admin_dashboard(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='/dashboard/')
def logout_user(request):
	logout(request)
	return redirect('dashboard:login_view')

@login_required(login_url='/dashboard/')                                                                                                                                                                                                                                                                                                                                                                                                                            
def change_password(request):
    if request.method == 'POST':
        change_password = ChangePasswordForm(data=request.POST, user=request.user)
        if change_password.is_valid():
            change_password.save()
            update_session_auth_hash(request, change_password.user)
            messages.success(request, 'Password Changed Successfully')
    else:
        change_password = ChangePasswordForm(user=request.user)
    return render(request, 'dashboard/change-password.html', {'change_pass':change_password})

@login_required(login_url='/dashboard/')                                                                                                                                                                                                                                                                                                                                                                                                                            
def add_admin(request):
    if request.method == 'POST':
        add_admin = AddAdmin(request.POST)
        if add_admin.is_valid():
            add_admin.save()
            messages.success(request, 'Admin Added Successfully')
    else:
        add_admin = AddAdmin()
    return render(request, 'dashboard/add-admin.html', {'admin_add':add_admin})


@login_required(login_url='/dashboard/')
def edit_form(request):
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('dashboard:view_profile')
    else:
        edit_form = EditProfileForm(instance=request.user)
    return render(request, 'dashboard/edit-admin-profile.html', {'edit':edit_form})

@login_required(login_url='/dashboard/')
def view_profile(request):
    return render(request, 'dashboard/view-profile.html', {'view':request.user})

