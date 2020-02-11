from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def all_products(request):
    """Renders a page with all products"""
    products = Product.objects.all()
    paginator = Paginator(products, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'page_obj': page_obj})
