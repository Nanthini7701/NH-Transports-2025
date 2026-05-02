from django.test import TestCase
from django.urls import reverse
from .models import ContactSubmission


class ContactSubmissionTestCase(TestCase):
    """Test cases for Contact Submission model"""
    
    def setUp(self):
        self.contact = ContactSubmission.objects.create(
            name="John Doe",
            phone="+1-800-1234567",
            pickup_location="Mumbai",
            drop_location="Delhi",
            message="Need transport for machinery"
        )
    
    def test_contact_creation(self):
        """Test if contact submission is created properly"""
        self.assertEqual(self.contact.name, "John Doe")
        self.assertEqual(self.contact.phone, "+1-800-1234567")
    
    def test_contact_string_representation(self):
        """Test contact string representation"""
        self.assertEqual(str(self.contact), "John Doe - +1-800-1234567")


class ViewsTestCase(TestCase):
    """Test cases for views"""
    
    def test_home_page_loads(self):
        """Test home page loads successfully"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_loads(self):
        """Test about page loads successfully"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_services_page_loads(self):
        """Test services page loads successfully"""
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
    
    def test_contact_page_loads(self):
        """Test contact page loads successfully"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
    
    def test_contact_form_submission(self):
        """Test contact form submission"""
        data = {
            'name': 'Test User',
            'phone': '+1-800-0000000',
            'pickup_location': 'Location A',
            'drop_location': 'Location B',
            'message': 'Test message'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(ContactSubmission.objects.count(), 1)
