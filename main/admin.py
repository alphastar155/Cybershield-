from django.contrib import admin
from .models import ContactMessage, ServiceRegistration

admin.site.site_header = "CyberShield Security Admin"
admin.site.site_title = "CyberShield Admin Portal"
admin.site.index_title = "Welcome to CyberShield Control Panel"

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')

@admin.register(ServiceRegistration)
class ServiceRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'service', 'registered_at')
    search_fields = ('full_name', 'email')
