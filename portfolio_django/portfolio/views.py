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
        from .models import Project
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Guilherme Nunes - Data Scientist'
        context['projects'] = Project.objects.filter(is_active=True)
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


class ProjectsPtView(TemplateView):
    """Página de projetos (Português)"""
    template_name = 'portfolio/projetos.html'

    def get_context_data(self, **kwargs):
        from .models import Project
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Projetos - Guilherme Nunes'
        context['language'] = 'pt'
        context['projects'] = Project.objects.filter(is_active=True)
        return context

class ProjectsEnView(TemplateView):
    """Projects page (English)"""
    template_name = 'portfolio/projects_en.html'

    def get_context_data(self, **kwargs):
        from .models import Project
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Projects - Guilherme Nunes'
        context['language'] = 'en'
        context['projects'] = Project.objects.filter(is_active=True)
        return context

class ProjectsEsView(TemplateView):
    """Página de proyectos (Español)"""
    template_name = 'portfolio/proyectos_es.html'

    def get_context_data(self, **kwargs):
        from .models import Project
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Proyectos - Guilherme Nunes'
        context['language'] = 'es'
        context['projects'] = Project.objects.filter(is_active=True)
        return context


# Views para diferentes idiomas
def home_pt(request):
    """Home em português"""
    from .models import Project, Certificate, Post
    stats = {
        'experience': '3+',
        'projects': Project.objects.filter(is_active=True).count(),
        'certifications': Certificate.objects.filter(is_active=True).count()
    }
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:2]
    return render(request, 'portfolio/home.html', {
        'language': 'pt',
        'page_title': 'Guilherme Nunes - Cientista de Dados',
        'stats': stats,
        'recent_posts': recent_posts
    })


def home_en(request):
    """Home em inglês"""
    from .models import Project, Certificate
    stats = {
        'experience': '3+',
        'projects': Project.objects.filter(is_active=True).count(),
        'certifications': Certificate.objects.filter(is_active=True).count()
    }
    return render(request, 'portfolio/home_en.html', {
        'language': 'en',
        'page_title': 'Guilherme Nunes - Data Scientist',
        'stats': stats
    })


def home_es(request):
    """Home em espanhol"""
    from .models import Project, Certificate
    stats = {
        'experience': '3+',
        'projects': Project.objects.filter(is_active=True).count(),
        'certifications': Certificate.objects.filter(is_active=True).count()
    }
    return render(request, 'portfolio/home_es.html', {
        'language': 'es',
        'page_title': 'Guilherme Nunes - Científico de Datos',
        'stats': stats
    })

class AboutView(TemplateView):
    """Página Sobre mim separada"""
    template_name = 'portfolio/sobre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Sobre - Guilherme Nunes'
        context['language'] = 'pt'
        return context

class AboutEnView(TemplateView):
    """English About page"""
    template_name = 'portfolio/about_en.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'About - Guilherme Nunes'
        context['language'] = 'en'
        return context

class AboutEsView(TemplateView):
    """Spanish About page"""
    template_name = 'portfolio/about_es.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Sobre - Guilherme Nunes'
        context['language'] = 'es'
        return context


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
