from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from .models import Item
from . import views
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
import logging  # Import the logging module

# Create your views here.


def index(request):
    items = Item.objects.all()

    return render(request, 'index.html', {'items': items})

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = 'Contact Us Form Submission'
        from_email = email  # Use the user's provided email as the sender
        recipient_email = 'dairotemitopedavid@gmail.com'  # Replace with the recipient's email address

        email_message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}'

        try:
            send_mail(subject, email_message, from_email, [recipient_email], fail_silently=False)
            return redirect('success_page')  # Redirect to a success page
            print("success")
        except Exception as e:
             error_message = f'An error occurred: {str(e)}'
             print(error_message)

    return render(request, 'contact.html')

def project(request):
    items = Item.objects.all()
    return render(request, 'project.html', {'items': items})

def service(request):
    return render(request, 'service.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def cart(request, item_id):
    items = get_object_or_404(Item, id=item_id)
    return render(request, 'cart.html', {'items' : items})

def ourterm(request):
    items = Item.objects.all()

    return render(request, 'ourterm.html', {'items':items})