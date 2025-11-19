"""
Configuração do Django Admin para portfolio
"""
from django.contrib import admin
from .models import Project, Certificate, Service, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin para projetos"""
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description', 'tags']
    list_editable = ['order', 'is_active']
    date_hierarchy = 'created_at'


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """Admin para certificados"""
    list_display = ['title', 'institution', 'date_issued', 'is_active']
    list_filter = ['institution', 'is_active', 'date_issued']
    search_fields = ['title', 'institution', 'description']
    list_editable = ['is_active']
    date_hierarchy = 'date_issued'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin para serviços"""
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin para mensagens de contato"""
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['is_read']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
