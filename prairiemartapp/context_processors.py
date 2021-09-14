from products.models import *
from products.forms import *


def categories(request):
    return {
        'categories': Category.objects.all()
    }



def search(request):
    query_form = FilterForm(request.GET)
    
    return { 'queryf': query_form }