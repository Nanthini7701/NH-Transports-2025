from django.contrib import admin
from .models import ContactSubmission, Testimonial


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'pickup_location', 'drop_location', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'pickup_location', 'drop_location')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'phone')
        }),
        ('Location Details', {
            'fields': ('pickup_location', 'drop_location')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'company', 'message')
    readonly_fields = ('created_at',)
