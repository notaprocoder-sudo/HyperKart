from django.shortcuts import render, redirect, get_object_or_404
from Fakekartapp.models import product
from .models import cart, Cartitem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def _cart_id(request):
    cartses = request.session.session_key
    if not cartses:
        cartses = request.session.create()
    return cartses


def add_to_cart(request, pro_id):
    product1 = get_object_or_404(product, id=pro_id)
    try:
        mycart = cart.objects.get(cart_id=_cart_id(request))
    except cart.DoesNotExist:
        mycart = cart.objects.create(cart_id=_cart_id(request))
        mycart.save(),
    try:
        cart_item = Cartitem.objects.get(product=product1, cart=mycart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item = Cartitem.objects.create(
            product=product1,
            quantity=1,
            cart=mycart
        )
        cart_item.save()
    return redirect('cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        mycart = cart.objects.get(cart_id=_cart_id(request))
        cart_items = Cartitem.objects.filter(cart=mycart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total, 'counter': counter})


def cart_remove(request, pro_id):
    mycart = cart.objects.get(cart_id=_cart_id(request))
    prod = get_object_or_404(product, id=pro_id)
    item = Cartitem.objects.get(product=prod, cart=mycart)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart:cart_detail')


def trash(request, pro_id):
    mycart = cart.objects.get(cart_id=_cart_id(request))
    prod = get_object_or_404(product, id=pro_id)
    item = Cartitem.objects.get(product=prod, cart=mycart)
    item.delete()
    return redirect('cart:cart_detail')
