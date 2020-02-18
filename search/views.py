from django.shortcuts import render
from products.models import Product
from django.contrib import messages
from django.core.paginator import Paginator


def do_search(request):
    if request.GET['q'] != '':
        products = Product.objects.filter(name__icontains=request.GET['q'])
        paginator = Paginator(products, 24)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products.html', {'page_obj': page_obj, 'products': products})
    else:
        messages.warning(request, 'Please enter a keyword to search for!')
        products = Product.objects.all()
        paginator = Paginator(products, 24)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products.html', {'page_obj': page_obj, 'products': products})
