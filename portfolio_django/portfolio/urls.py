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
    path('receitas/', views.ReceitasView.as_view(), name='receitas'),
]
