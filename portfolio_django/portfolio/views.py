"""
Views para o portfolio
"""
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import JsonResponse
from .models import Post, Visitor


def language_selector(request):
    """Tela de seleção de idioma"""
    return render(request, 'portfolio/language_selector.html', {
        'page_title': 'Select Your Language - Guilherme Nunes'
    })


class HomeView(TemplateView):
    """View principal do portfolio"""
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Guilherme Nunes - Data Scientist'
        context['stats'] = {
            'experience': '3+',
            'projects': '15+',
            'certifications': '10+'
        }
        return context


class CertificadosView(TemplateView):
    """View para página de certificados"""
    template_name = 'portfolio/certificados.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Certificados - Guilherme Nunes'
        return context


class RedesSociaisView(TemplateView):
    """View para página de redes sociais"""
    template_name = 'portfolio/redes_sociais.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Redes Sociais - Guilherme Nunes'
        return context


class ReceitasView(TemplateView):
    """View para assistente de receitas"""
    template_name = 'portfolio/receitas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Assistente de Receitas - Guilherme Nunes'
        return context


# Views para diferentes idiomas
def home_pt(request):
    """Home em português"""
    return render(request, 'portfolio/home.html', {
        'language': 'pt',
        'page_title': 'Guilherme Nunes - Cientista de Dados'
    })


def home_en(request):
    """Home em inglês"""
    return render(request, 'portfolio/home_en.html', {
        'language': 'en',
        'page_title': 'Guilherme Nunes - Data Scientist'
    })


def home_es(request):
    """Home em espanhol"""
    return render(request, 'portfolio/home_es.html', {
        'language': 'es',
        'page_title': 'Guilherme Nunes - Científico de Datos'
    })


class BlogView(ListView):
    """View para lista de posts do blog"""
    model = Post
    template_name = 'portfolio/blog.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(published=True)


class BlogDetailView(DetailView):
    """View para detalhes de um post do blog"""
    model = Post
    template_name = 'portfolio/blog_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'


class VisitorMapView(TemplateView):
    """View para mapa de visitantes"""
    template_name = 'portfolio/mapa_visitantes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Mapa de Visitantes - Guilherme Nunes'
        return context


def visitor_data_api(request):
    """API para retornar dados dos visitantes em formato JSON para o mapa"""
    visitors = Visitor.objects.filter(
        latitude__isnull=False,
        longitude__isnull=False
    ).values('country', 'region', 'city', 'latitude', 'longitude', 'visited_at')
    
    # Agrupa visitantes por localização
    locations = {}
    for visitor in visitors:
        key = f"{visitor['latitude']},{visitor['longitude']}"
        if key not in locations:
            locations[key] = {
                'latitude': float(visitor['latitude']),
                'longitude': float(visitor['longitude']),
                'country': visitor['country'],
                'region': visitor['region'],
                'city': visitor['city'],
                'count': 1,
                'last_visit': visitor['visited_at'].isoformat()
            }
        else:
            locations[key]['count'] += 1
            if visitor['visited_at'].isoformat() > locations[key]['last_visit']:
                locations[key]['last_visit'] = visitor['visited_at'].isoformat()
    
    return JsonResponse({'locations': list(locations.values())})
