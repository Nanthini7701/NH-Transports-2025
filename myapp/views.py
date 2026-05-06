from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.db import OperationalError, connection
from .models import ContactSubmission, Testimonial
from django.core.mail import send_mail
from django.core.mail import EmailMessage
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
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        pickup_location = request.POST.get("pickup_location", "").strip()
        drop_location = request.POST.get("drop_location", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not phone or not pickup_location or not drop_location or not message:
            messages.error(request, "Please fill all required fields.")
            return redirect("contact")

        subject = f"New Enquiry from NH Transports - {name}"

        body = f"""
New message from NH Transports website

Name: {name}
Phone: {phone}
Pickup Location: {pickup_location}
Drop Location: {drop_location}

Message:
{message}
"""

        try:
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_RECEIVER_EMAIL],
                reply_to=[settings.EMAIL_HOST_USER],
            )
            email.send(fail_silently=False)

            messages.success(request, "Message sent successfully!")
            return redirect("contact")

        except Exception as e:
            print("EMAIL SENDING ERROR:", e)
            messages.error(request, "Message not sent. Please check Gmail app password or Railway email variables.")
            return redirect("contact")

    return render(request, "contact.html")