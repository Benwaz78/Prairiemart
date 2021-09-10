from django import forms
from django.core import validators
from django.conf import settings
from dashboard.models import *
from django.contrib.auth.forms import(
    PasswordResetForm, SetPasswordForm, PasswordChangeForm, 
    UserChangeForm, UserCreationForm)


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Email'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    def clean_email(self):
        email = self.cleaned_data['email']
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email does not  exist')  
        return email

    
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm Password'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Old Password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


class AddAdmin(UserCreationForm):
    user_name = forms.CharField(label='Username*', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password1 = forms.CharField(label='Enter Password*', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password*', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    email = forms.CharField(label='Email*', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}))
    phone = forms.CharField(label='Phone Number*', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    profile = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = CustomUser
        fields = ('user_name', 'password1', 'password2', 'email', 'first_name', 'last_name', 'phone')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_name = self.cleaned_data['user_name']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()
            return user

class EditProfileForm(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'user_name'}))
    first_name = forms.CharField(label='Firstname', required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}))
    last_name = forms.CharField(label='Lastname', required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}))
    email = forms.CharField(label='Email*', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    phone = forms.CharField(label='Phone Number*', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    profile = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = CustomUser
        fields = ('user_name', 'first_name', 'last_name', 'email', 'profile', 'phone')

    