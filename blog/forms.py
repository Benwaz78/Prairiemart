from cProfile import label
from unicodedata import category
from django import forms
from blog.models import *
from django.core import validators


class PostForm(forms.ModelForm):
    pst_title = forms.CharField(
        label='Post title',
        widget = forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    pst_image = forms.ImageField(
        label ='Post Image',
        widget = forms.ClearableFileInput(
            attrs={'class':'form-control'}
        )
    ) 
    category = forms.ModelMultipleChoiceField(
		queryset=Category.objects.all(), 
		widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
		label='Select Category'
		)
    content = forms.CharField(
        label = 'Content',
        widget = forms.Textarea(
            attrs = {'class':'form-control'}
        )
    )

    class Meta():
        model = Post
        exclude = ('created','time','user','slug',)


class PostCategoryForm(forms.ModelForm):
    cat_name = forms.CharField(
        label='Category Name*',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category Name'})
    )
    cat_name = forms.CharField(
        label='Category Description*',
        widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Category Description'})
    )
    
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = Category
        fields = '__all__'