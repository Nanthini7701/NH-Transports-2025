from django.core.management.base import BaseCommand
from myapp.models import Testimonial

class Command(BaseCommand):
    help = 'Populate sample testimonials'

    def handle(self, *args, **options):
        if Testimonial.objects.count() == 0:
            testimonials = [
                {
                    'name': 'Rajesh Kumar',
                    'company': 'Tech Solutions Ltd',
                    'message': 'NH Transports provided excellent service for our interstate cargo delivery. The team was professional, timely, and our goods arrived in perfect condition.',
                    'rating': 5
                },
                {
                    'name': 'Priya Sharma',
                    'company': 'Fashion Hub',
                    'message': 'We have been using NH Transports for our local deliveries for over a year now. Their reliability and customer service is outstanding.',
                    'rating': 5
                },
                {
                    'name': 'Mohan Reddy',
                    'company': 'Construction Co',
                    'message': 'The heavy equipment transport service was handled with great care and expertise. Highly recommended for industrial transport needs.',
                    'rating': 5
                },
                {
                    'name': 'Anita Patel',
                    'company': 'Retail Chain',
                    'message': 'Fast, secure, and affordable transport solutions. NH Transports has become our go-to partner for all logistics requirements.',
                    'rating': 4
                },
                {
                    'name': 'Vikram Singh',
                    'company': 'Manufacturing Inc',
                    'message': 'Professional team with modern tracking systems. Our shipments are always delivered on time with complete transparency.',
                    'rating': 5
                },
                {
                    'name': 'Kavita Nair',
                    'company': 'E-commerce Store',
                    'message': 'Excellent customer support and competitive pricing. The cargo management services are top-notch.',
                    'rating': 5
                }
            ]

            for testimonial_data in testimonials:
                Testimonial.objects.create(**testimonial_data)

            self.stdout.write(
                self.style.SUCCESS('Successfully populated 6 sample testimonials')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Testimonials already exist, skipping population')
            )