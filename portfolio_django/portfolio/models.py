"""
Models para o portfolio
"""
from django.db import models
from django.urls import reverse


class Project(models.Model):
    """Modelo para projetos do portfolio"""
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    image = models.ImageField('Imagem', upload_to='projects/')
    url = models.URLField('URL do Projeto', blank=True)
    tags = models.CharField('Tags', max_length=200, help_text='Separadas por vírgula')
    order = models.IntegerField('Ordem', default=0)
    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_tags_list(self):
        """Retorna tags como lista"""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]


class Certificate(models.Model):
    """Modelo para certificados"""
    title = models.CharField('Título', max_length=200)
    institution = models.CharField('Instituição', max_length=200)
    description = models.TextField('Descrição', blank=True)
    image = models.ImageField('Imagem', upload_to='certificates/')
    url = models.URLField('URL do Certificado', blank=True)
    date_issued = models.DateField('Data de Emissão')
    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'
        ordering = ['-date_issued']
    
    def __str__(self):
        return f"{self.title} - {self.institution}"


class Service(models.Model):
    """Modelo para serviços oferecidos"""
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    icon = models.CharField('Ícone (classe boxicons)', max_length=100, 
                           help_text="Ex: bx-data, bxs-dashboard")
    order = models.IntegerField('Ordem', default=0)
    is_active = models.BooleanField('Ativo', default=True)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['order']
    
    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Modelo para mensagens de contato"""
    name = models.CharField('Nome', max_length=200)
    email = models.EmailField('Email')
    subject = models.CharField('Assunto', max_length=200)
    message = models.TextField('Mensagem')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    is_read = models.BooleanField('Lida', default=False)
    
    class Meta:
        verbose_name = 'Mensagem de Contato'
        verbose_name_plural = 'Mensagens de Contato'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class Post(models.Model):
    """Modelo para posts do blog"""
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', max_length=220, unique=True)
    excerpt = models.TextField('Resumo', blank=True)
    content = models.TextField('Conteúdo')
    cover_image = models.ImageField('Imagem de capa', upload_to='blog/', blank=True, null=True)
    published = models.BooleanField('Publicado', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('portfolio:blog_detail', kwargs={'slug': self.slug})


class Visitor(models.Model):
    """Modelo para rastreamento de visitantes"""
    ip_address = models.GenericIPAddressField('Endereço IP', unique=True)
    country = models.CharField('País', max_length=100, blank=True)
    country_code = models.CharField('Código do País', max_length=10, blank=True)
    region = models.CharField('Região/Estado', max_length=100, blank=True)
    city = models.CharField('Cidade', max_length=100, blank=True)
    latitude = models.DecimalField('Latitude', max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField('Longitude', max_digits=9, decimal_places=6, null=True, blank=True)
    user_agent = models.TextField('User Agent', blank=True)
    visit_count = models.IntegerField('Contagem de Visitas', default=1)
    first_visit = models.DateTimeField('Primeira Visita', auto_now_add=True)
    last_visit = models.DateTimeField('Última Visita', auto_now=True)
    visited_at = models.DateTimeField('Visitado em', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        ordering = ['-last_visit']
    
    def __str__(self):
        return f"{self.ip_address} - {self.city}, {self.country} ({self.visit_count} visitas)"


class Course(models.Model):
    """Modelo para cursos"""
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', max_length=220, unique=True)
    description = models.TextField('Descrição')
    cover_image = models.ImageField('Imagem de capa', upload_to='courses/', blank=True, null=True)
    order = models.IntegerField('Ordem', default=0)
    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('portfolio:course_detail', kwargs={'slug': self.slug})
    
    def get_lessons_count(self):
        """Retorna o número de aulas do curso"""
        return self.lessons.filter(is_active=True).count()


class Lesson(models.Model):
    """Modelo para aulas de um curso"""
    VIDEO_TYPE_CHOICES = [
        ('youtube', 'YouTube'),
        ('upload', 'Vídeo Enviado'),
    ]
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Curso')
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    video_type = models.CharField('Tipo de Vídeo', max_length=10, choices=VIDEO_TYPE_CHOICES, default='youtube')
    youtube_url = models.URLField('URL do YouTube', blank=True, help_text='Ex: https://www.youtube.com/watch?v=VIDEO_ID')
    video_file = models.FileField('Arquivo de Vídeo', upload_to='lessons/videos/', blank=True, null=True)
    order = models.IntegerField('Ordem', default=0)
    duration = models.CharField('Duração', max_length=20, blank=True, help_text='Ex: 15:30')
    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['order', 'created_at']
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"
    
    def get_youtube_embed_url(self):
        """Converte URL do YouTube para formato embed"""
        if self.youtube_url and 'youtube.com' in self.youtube_url:
            if 'watch?v=' in self.youtube_url:
                video_id = self.youtube_url.split('watch?v=')[1].split('&')[0]
                return f"https://www.youtube.com/embed/{video_id}"
            elif 'youtu.be/' in self.youtube_url:
                video_id = self.youtube_url.split('youtu.be/')[1].split('?')[0]
                return f"https://www.youtube.com/embed/{video_id}"
        return self.youtube_url