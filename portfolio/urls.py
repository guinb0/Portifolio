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
    path('en/certificates/', views.CertificadosEnView.as_view(), name='certificates_en'),
    path('es/certificados/', views.CertificadosEsView.as_view(), name='certificados_es'),
    path('redes/', views.RedesSociaisView.as_view(), name='redes_sociais'),
    path('en/social/', views.SocialEnView.as_view(), name='social_en'),
    path('es/redes/', views.SocialEsView.as_view(), name='redes_es'),
    path('projetos/', views.ProjectsPtView.as_view(), name='projetos'),
    path('en/projects/', views.ProjectsEnView.as_view(), name='projects_en'),
    path('es/proyectos/', views.ProjectsEsView.as_view(), name='proyectos_es'),
    path('sobre/', views.AboutView.as_view(), name='sobre'),
    path('en/about/', views.AboutEnView.as_view(), name='about_en'),
    path('es/sobre/', views.AboutEsView.as_view(), name='about_es'),
    
    # Cursos
    path('cursos/', views.CoursesView.as_view(), name='cursos'),
    path('en/courses/', views.CoursesEnView.as_view(), name='courses_en'),
    path('es/cursos/', views.CoursesEsView.as_view(), name='cursos_es'),
    path('cursos/<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('en/courses/<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail_en'),
    path('es/cursos/<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail_es'),
    
    # Blog
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('en/blog/', views.BlogEnView.as_view(), name='blog_en'),
    path('en/blog/<slug:slug>/', views.BlogDetailEnView.as_view(), name='blog_detail_en'),
    path('es/blog/', views.BlogEsView.as_view(), name='blog_es'),
    path('es/blog/<slug:slug>/', views.BlogDetailEsView.as_view(), name='blog_detail_es'),
    
    # Mapa de visitantes
    path('mapa-visitantes/', views.VisitorMapView.as_view(), name='mapa_visitantes'),
    path('en/visitors-map/', views.VisitorMapEnView.as_view(), name='visitors_map_en'),
    path('es/mapa-visitantes/', views.VisitorMapEsView.as_view(), name='mapa_visitantes_es'),
    path('api/visitor-data/', views.visitor_data_api, name='visitor_data_api'),
    path('api/register-visitor/', views.register_visitor, name='register_visitor'),
]