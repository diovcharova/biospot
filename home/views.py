from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages
import os


def homepage(request):
    """Return the home.html file"""
    return render(request, 'home.html')


def contactspage(request):
    """Return a contact form"""
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            messages.success(request, 'Your message was successfully sent!')
            return redirect('contactspage')
        else:
            messages.error(request, "Your message was NOT sent!")
    else:
        form = ContactForm()
    API_KEY = os.environ.get('GOOGLE_API')
    return render(request, 'contacts.html', {'form': form, 'API_KEY': API_KEY})
