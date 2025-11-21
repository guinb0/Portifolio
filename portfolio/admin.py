"""
Configuração do Django Admin para portfolio
"""
from django.contrib import admin
from .models import Project, Certificate, Service, ContactMessage, Post, Visitor, Course, Lesson, SiteConfig


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


class LessonInline(admin.TabularInline):
    """Inline para aulas dentro do curso"""
    model = Lesson
    extra = 1
    fields = ['title', 'order', 'video_type', 'youtube_url', 'video_file', 'duration', 'is_active']
    ordering = ['order']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin para cursos"""
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    inlines = [LessonInline]
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'slug', 'description', 'cover_image')
        }),
        ('Configurações', {
            'fields': ('order', 'is_active')
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Admin para aulas"""
    list_display = ['title', 'course', 'order', 'video_type', 'duration', 'is_active', 'created_at']
    list_filter = ['course', 'video_type', 'is_active', 'created_at']
    search_fields = ['title', 'description', 'course__title']
    list_editable = ['order', 'is_active']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('course', 'title', 'description', 'order', 'duration')
        }),
        ('Vídeo', {
            'fields': ('video_type', 'youtube_url', 'video_file'),
            'description': 'Escolha o tipo de vídeo e preencha o campo correspondente'
        }),
        ('Configurações', {
            'fields': ('is_active',)
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    """Admin para configurações do site (Singleton)"""
    
    def has_add_permission(self, request):
        """Impede criação de mais instâncias"""
        return not SiteConfig.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        """Impede deleção"""
        return False
    
    fieldsets = (
        ('Cargo/Título', {
            'fields': ('job_title_pt', 'job_title_en', 'job_title_es'),
            'description': 'Seu cargo profissional exibido na home'
        }),
        ('Slogan', {
            'fields': ('slogan_pt', 'slogan_en', 'slogan_es'),
            'description': 'Frase de efeito exibida na home'
        }),
        ('Imagem', {
            'fields': ('profile_image',),
            'description': 'Foto de perfil exibida no site'
        }),
        ('Sobre (Seção About)', {
            'fields': ('about_pt', 'about_en', 'about_es'),
            'description': 'Texto da seção sobre em cada idioma'
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']
