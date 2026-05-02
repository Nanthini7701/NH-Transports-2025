from django.db import models

class ContactSubmission(models.Model):
    """Model to store contact form submissions"""
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contact Submissions"
    
    def __str__(self):
        return f"{self.name} - {self.phone}"


class Testimonial(models.Model):
    """Model to store customer testimonials"""
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
