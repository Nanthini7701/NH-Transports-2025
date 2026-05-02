from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import ContactSubmission, Testimonial


def home(request):
    """Home page view"""
    testimonials = Testimonial.objects.all()[:6]
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
            # Create contact submission
            ContactSubmission.objects.create(
                name=name,
                phone=phone,
                pickup_location=pickup_location,
                drop_location=drop_location,
                message=message
            )
            messages.success(request, 'Thank you! We will contact you shortly.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill all required fields.')
    
    context = {
        'page_title': 'Contact Us'
    }
    return render(request, 'contact.html', context)
