from .models import cart, Cartitem
from .views import _cart_id


def counter(request):
    itemcount=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            mycart=cart.objects.filter(cart_id=_cart_id(request))
            mycartitem=Cartitem.objects.all().filter(cart=mycart[:1])
            for cartitem in mycartitem:
                itemcount += cartitem.quantity
        except cart.DoesNotExist:
            itemcount =0
    return dict(itemcount=itemcount)
