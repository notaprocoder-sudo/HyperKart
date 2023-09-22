from django.shortcuts import render, get_object_or_404
from .models import category, product
from django.core.paginator import Paginator,EmptyPage,InvalidPage



# Create your views here.

def AllProdCat(request, c_slug=None):
    c_page = None
    p_page = None
    if c_slug != None:
        c_page = get_object_or_404(category, slug=c_slug)
        p_page = product.objects.all().filter(category=c_page, available=True)
    else:
        p_page = product.objects.all().filter(available=True)
    paginator=Paginator(p_page,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'cate': c_page, 'prod': products})


def prodetail(request, c_slug, p_slug):
    try:
        det = product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(request, 'details.html', {'detail': det})
