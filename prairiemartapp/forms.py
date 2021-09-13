from django import forms
from django.core import validators
from dashboard.models import *




class EditCustomerProfileForm(forms.ModelForm):
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.profile = self.cleaned_data['profile']
        

        if commit:
            user.save()
            return user

