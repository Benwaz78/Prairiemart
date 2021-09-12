from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.views.generic import(
    ListView, UpdateView, CreateView,
    DetailView, DeleteView, View
)

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

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
    return render(request, 'dashboard/users/add-admin.html', {'admin_add':add_admin})


@login_required(login_url='/dashboard/')
def edit_form(request):
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('dashboard:view_profile')
    else:
        edit_form = EditProfileForm(instance=request.user)
    return render(request, 'dashboard/users/edit-admin-profile.html', {'edit':edit_form})

@login_required(login_url='/dashboard/')
def edit_vendor_profile_form(request):
    if request.method == 'POST':
        edit_form = EditVendorProfileForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('dashboard:view_profile')
    else:
        edit_form = EditVendorProfileForm(instance=request.user)
    return render(request, 'dashboard/users/edit-vendor-profile.html', {'edit_vendor':edit_form})

@login_required(login_url='/dashboard/')
def view_profile(request):
    return render(request, 'dashboard/users/view-profile.html', {'view':request.user})


class ListUsers(LoginRequiredMixin, ListView):
    login_url = '/dashboard/'
    model= CustomUser
    paginate_by = 4
    template_name = 'dashboard/users/list-users.html'
    context_object_name='list_users'

class SingleUser(LoginRequiredMixin, DetailView):
    login_url = '/dashboard/'
    model= CustomUser
    template_name = 'dashboard/users/single-user.html'
    context_object_name='single_user'

class DeleteUser(LoginRequiredMixin, DeleteView):
    login_url = '/dashboard/'
    model= CustomUser
    success_url = reverse_lazy('dashboard:list_users')


class AddVendorView(SuccessMessageMixin, CreateView):
    model= CustomUser
    template_name = 'auth/register-vendor.html'
    form_class = AddAdmin
    success_message = 'You have registered successfully'
    success_url = reverse_lazy('dashboard:add_vendor')

    def form_valid(self, form):
        form.instance.is_staff = False
        form.instance.is_vendor = True
        form.instance.is_active = True
        return super().form_valid(form)

class UpdateUser(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    model= CustomUser
    template_name = 'dashboard/users/update-user-profile.html'
    form_class = EditProfileForm
    success_message = 'User have been updated successfully'
    success_url = reverse_lazy('dashboard:single_user')

    def form_valid(self, form):
        form.instance.is_staff = False
        form.instance.is_vendor = True
        form.instance.is_active = True
        return super().form_valid(form)

def activate_user(request, user_id):
    get_user = get_object_or_404(CustomUser, id=user_id)
    get_user.activate_user()
    return redirect('dashboard:list_users')

def deactivate_user(request, user_id):
    get_user = get_object_or_404(CustomUser, id=user_id)
    get_user.deactivate_user()
    return redirect('dashboard:list_users')




    