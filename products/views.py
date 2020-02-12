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


def products_skincare_and_beauty(request):
    """Renders a page with products from skincare and beauty category"""
    products = Product.objects.filter(categories="1")
    paginator = Paginator(products, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products_skincare_and_beauty.html', {'products': products,'page_obj': page_obj})


def products_bulk(request):
    """Renders a page with products from bulk foods category"""
    products = Product.objects.filter(categories="5")
    paginator = Paginator(products, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products_bulk.html', {'products': products,'page_obj': page_obj})


def products_cleaning_and_household(request):
    """Renders a page with products from cleaning and household category"""
    products = Product.objects.filter(categories="6")
    paginator = Paginator(products, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products_cleaning_and_household.html', {'products': products,'page_obj': page_obj})


def products_organic(request):
    """Renders a page with products from organic foods category"""
    products = Product.objects.filter(categories="4")
    paginator = Paginator(products, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products_organic.html', {'products': products,'page_obj': page_obj})


def products_supplements(request):
    """Renders a page with products from supplements category"""
    products = Product.objects.filter(categories="3")
    paginator = Paginator(products, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products_supplements.html', {'products': products,'page_obj': page_obj})


def products_raw_and_superfoods(request):
    """Renders a page with products from raw and superfoods category"""
    products = Product.objects.filter(categories="2")
    paginator = Paginator(products, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products_raw_and_superfoods.html', {'products': products,'page_obj': page_obj})
