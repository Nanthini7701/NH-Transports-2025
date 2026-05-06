from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.db import OperationalError, connection
from .models import ContactSubmission, Testimonial
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    """Home page view"""
    testimonials = []
    try:
        table_names = connection.introspection.table_names()
        if 'myapp_testimonial' in table_names:
            testimonials = list(Testimonial.objects.all()[:6])
    except OperationalError:
        # Database tables not yet created - display page without testimonials
        testimonials = []
    except Exception:
        # Any other database error
        testimonials = []
    
    context = {
        'testimonials': testimonials,
        'page_title': 'Home'
    }
    return render(request, 'home.html', context)


def about(request):
    """About page view"""
    context = {
        'page_title': 'About Us'
    }
    return render(request, 'about.html', context)


def services(request):
    """Services page view"""
    services_list = [
        {
            'title': 'Local Transport',
            'description': 'Reliable local transportation for all your needs.',
            'icon': 'local'
        },
        {
            'title': 'Interstate Transport',
            'description': 'Safe and timely interstate cargo delivery.',
            'icon': 'interstate'
        },
        {
            'title': 'Heavy Equipment',
            'description': 'Specialized transport for heavy machinery.',
            'icon': 'heavy'
        },
        {
            'title': 'Cargo Management',
            'description': 'Complete cargo handling and storage solutions.',
            'icon': 'cargo'
        },
        {
            'title': 'Climate Controlled',
            'description': 'Temperature controlled transport for sensitive goods.',
            'icon': 'climate'
        },
        {
            'title': '24/7 Support',
            'description': 'Round-the-clock customer support and tracking.',
            'icon': 'support'
        },
    ]
    
    context = {
        'services': services_list,
        'page_title': 'Services'
    }
    return render(request, 'services.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        pickup_location = request.POST.get("pickup_location")
        drop_location = request.POST.get("drop_location")
        message = request.POST.get("message")

        subject = f"New Contact Message from {name}"

        email_message = f"""
New enquiry from NH Transports website

Name: {name}
Phone: {phone}
Pickup Location: {pickup_location}
Drop Location: {drop_location}

Message:
{message}
"""

        try:
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")

        except Exception as e:
            messages.error(request, "Message sending failed. Please try again.")
            print("Email error:", e)

    return render(request, "contact.html")