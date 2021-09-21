from django import template
from products.models import *

register = template.Library()


@register.inclusion_tag('prairiemartapp/prairiemart_tags/menu-tag.html')
def display_menu():
	categories = Category.objects.all()
	return {'categories_on_menu':categories}


@register.inclusion_tag('prairiemartapp/prairiemart_tags/brand-sidebar-tag.html')
def list_brand_on_sidebar():
	brands = Brand.objects.all()
	return {'brands':brands}

