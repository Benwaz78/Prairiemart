from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect

from products.models import Products
from basket.forms import CartAddProductForm
from orders.models import Order, OrderItem

from .basket import Basket
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@require_POST
def basket_add(request,product_id):
    basket = Basket(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    # if request.POST.get('action') == 'post':
    #     quantity = int(request.POST.get('qty'))
        # basket.add(product=product, qty=quantity)

        # basketqty = basket.__len__()
        # response = JsonResponse({'qty': basketqty})
    return redirect('basket:basket_summary')


def basket_delete(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Products, id=product_id)
    basket.delete(product)
    return redirect('basket:basket_summary')

    # if request.POST.get('action') == 'post':
    #     product_id = int(request.POST.get('productid'))
    #     basket.delete(product=product_id)

    #     basketqty = basket.__len__()
    #     baskettotal = basket.get_total_price()
    #     response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        # return response

def basket_summary(request):
    basket = Basket(request)
    for item in basket:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'prairiemartapp/summary.html', {'basket': basket})

# def basket_update(request):
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('product_id'))
#         quantity = int(request.POST.get('quantity'))
#         basket.update(product=product_id, quantity=quantity)

#         basketqty = basket.__len__()
#         baskettotal = basket.get_total_price()
#         response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
#         return response