"""
URLs da app portfolio
"""
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # Página principal (português)
    path('', views.home_pt, name='home'),
    
    # Páginas em outros idiomas
    path('EN/', views.home_en, name='home_en'),
    path('ES/', views.home_es, name='home_es'),
    
    # Outras páginas
    path('certificados/', views.CertificadosView.as_view(), name='certificados'),
    path('redes/', views.RedesSociaisView.as_view(), name='redes_sociais'),
    path('receitas/', views.ReceitasView.as_view(), name='receitas'),
]
