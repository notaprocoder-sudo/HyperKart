from django.shortcuts import render
from Fakekartapp.models import product
from django.db.models import Q


# Create your views here.


def search_result(request):
    product1 = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        product1 = (product.objects.all()).filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'query': query, 'products': product1})
