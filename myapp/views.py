from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.db import OperationalError, connection
from .models import ContactSubmission, Testimonial


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
    """Contact page view - handles both GET and POST"""
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        pickup_location = request.POST.get('pickup_location', '')
        drop_location = request.POST.get('drop_location', '')
        message = request.POST.get('message', '')
        
        # Validate form data
        if name and phone and pickup_location and drop_location and message:
            try:
                # Create contact submission
                ContactSubmission.objects.create(
                    name=name,
                    phone=phone,
                    pickup_location=pickup_location,
                    drop_location=drop_location,
                    message=message
                )
                messages.success(request, 'Thank you! We will contact you shortly.')
            except OperationalError:
                messages.error(request, 'Database is initializing. Please try again in a moment.')
            except Exception as e:
                messages.error(request, 'An error occurred while submitting the form. Please try again.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill all required fields.')
    
    context = {
        'page_title': 'Contact Us'
    }
    return render(request, 'contact.html', context)
