from django.shortcuts import render
from .forms import ContactForm


def homepage(request):
    """Return the home.html file"""
    return render(request, 'home.html')


def contactspage(request):
    """Return a contact form"""
    form = ContactForm
    return render(request, 'contacts.html', {'form': form})
