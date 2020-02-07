from django.shortcuts import render
from .models import Product


def all_products(request):
    """Renders a page with all products"""
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
