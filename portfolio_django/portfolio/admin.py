"""
Configuração do Django Admin para portfolio
"""
from django.contrib import admin
from .models import Project, Certificate, Service, ContactMessage, Post, Visitor


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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin para posts do blog"""
    list_display = ['title', 'published', 'created_at', 'updated_at']
    list_filter = ['published', 'created_at']
    search_fields = ['title', 'excerpt', 'content']
    list_editable = ['published']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    """Admin para visitantes"""
    list_display = ['ip_address', 'country', 'region', 'city', 'visited_at']
    list_filter = ['country', 'visited_at']
    search_fields = ['ip_address', 'country', 'region', 'city']
    date_hierarchy = 'visited_at'
    readonly_fields = ['ip_address', 'country', 'country_code', 'region', 'city', 
                      'latitude', 'longitude', 'user_agent', 'visited_at']
