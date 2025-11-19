"""
Models para o portfolio
"""
from django.db import models


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
