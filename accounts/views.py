from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages


def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')


def logout(request):
    """To logout the user and redirect back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
