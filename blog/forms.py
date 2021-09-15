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
    # category = forms.ModelMultipleChoiceField(
	# 	queryset=Category.objects.all(), 
	# 	widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
	# 	empty_label='Select Category'
	# 	)
    # content = forms.CharField(
    #     label = 'Content',
    #     widget = forms.Textarea(
    #         attrs = {'class':'form-control'}
    #     )
    # )

    class Meta():
        model = Post
        exclude = ('created','time','user','slug',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Email'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }