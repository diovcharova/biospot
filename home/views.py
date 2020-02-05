from django.shortcuts import render


def homepage(request):
    """Return the home.html file"""
    return render(request, 'home.html')
