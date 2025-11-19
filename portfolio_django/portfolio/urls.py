"""
URLs da app portfolio
"""
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # Seleção de idioma (primeira tela)
    path('', views.language_selector, name='language_selector'),
    
    # Páginas em diferentes idiomas
    path('pt/', views.home_pt, name='home'),
    path('en/', views.home_en, name='home_en'),
    path('es/', views.home_es, name='home_es'),
    
    # Outras páginas
    path('certificados/', views.CertificadosView.as_view(), name='certificados'),
    path('redes/', views.RedesSociaisView.as_view(), name='redes_sociais'),
    path('projetos/', views.ProjectsPtView.as_view(), name='projetos'),
    path('en/projects/', views.ProjectsEnView.as_view(), name='projects_en'),
    path('es/proyectos/', views.ProjectsEsView.as_view(), name='proyectos_es'),
    path('sobre/', views.AboutView.as_view(), name='sobre'),
    path('en/about/', views.AboutEnView.as_view(), name='about_en'),
    path('es/sobre/', views.AboutEsView.as_view(), name='about_es'),
    
    # Blog
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    
    # Mapa de visitantes
    path('mapa-visitantes/', views.VisitorMapView.as_view(), name='mapa_visitantes'),
    path('api/visitor-data/', views.visitor_data_api, name='visitor_data_api'),
]
