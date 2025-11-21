"""
Views para o portfolio
"""
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Post, Visitor
import requests


def get_client_ip(request):
    """Extrai o IP real do visitante, considerando proxies"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@csrf_exempt
def register_visitor(request):
    """Registra um novo visitante no banco de dados"""
    if request.method == 'POST':
        try:
            ip_address = get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            
            # Ignora IPs locais
            if ip_address in ['127.0.0.1', 'localhost', '::1']:
                return JsonResponse({'status': 'ignored', 'message': 'Local IP'})
            
            # Busca geolocalização do IP usando API gratuita
            try:
                response = requests.get(f'http://ip-api.com/json/{ip_address}', timeout=5)
                geo_data = response.json()
                
                if geo_data.get('status') == 'success':
                    # Verifica se já existe um visitante com este IP
                    visitor, created = Visitor.objects.get_or_create(
                        ip_address=ip_address,
                        defaults={
                            'city': geo_data.get('city', 'Desconhecido'),
                            'region': geo_data.get('regionName', ''),
                            'country': geo_data.get('country', 'Desconhecido'),
                            'country_code': geo_data.get('countryCode', ''),
                            'latitude': geo_data.get('lat', 0),
                            'longitude': geo_data.get('lon', 0),
                            'user_agent': user_agent,
                            'visit_count': 1
                        }
                    )
                    
                    # Se já existia, atualiza a contagem e última visita
                    if not created:
                        visitor.visit_count += 1
                        visitor.last_visit = timezone.now()
                        visitor.user_agent = user_agent
                        visitor.save()
                    
                    return JsonResponse({
                        'status': 'success',
                        'created': created,
                        'visit_count': visitor.visit_count,
                        'location': f"{visitor.city}, {visitor.country}"
                    })
                else:
                    return JsonResponse({'status': 'error', 'message': 'Geolocation failed'})
                    
            except requests.RequestException as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
                
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


def visitor_data_api(request):
    """API para retornar dados dos visitantes em formato JSON para o mapa"""
    visitors = Visitor.objects.filter(
        latitude__isnull=False,
        longitude__isnull=False
    )
    
    # Agrupa visitantes por localização (IP único) ignorando múltiplas visitas
    locations = {}
    unique_ips_global = set()
    total_visits = 0
    for visitor in visitors:
        total_visits += visitor.visit_count  # total de hits
        unique_ips_global.add(visitor.ip_address)
        key = f"{visitor.latitude},{visitor.longitude}"
        if key not in locations:
            locations[key] = {
                'latitude': float(visitor.latitude),
                'longitude': float(visitor.longitude),
                'country': visitor.country,
                'region': visitor.region,
                'city': visitor.city,
                'unique_ips': {visitor.ip_address},  # conjunto para contar únicos
                'unique_count': 1,
                'total_visits': visitor.visit_count,
                'last_visit': visitor.last_visit.isoformat()
            }
        else:
            # Adiciona IP ao conjunto; atualiza contadores e última visita
            if visitor.ip_address not in locations[key]['unique_ips']:
                locations[key]['unique_ips'].add(visitor.ip_address)
                locations[key]['unique_count'] += 1
            locations[key]['total_visits'] += visitor.visit_count
            if visitor.last_visit.isoformat() > locations[key]['last_visit']:
                locations[key]['last_visit'] = visitor.last_visit.isoformat()

    # Normaliza saída (remove sets)
    location_list = []
    for loc in locations.values():
        loc['unique_ips'] = len(loc['unique_ips'])
        location_list.append(loc)

    return JsonResponse({
        'locations': location_list,
        'summary': {
            'unique_ips_global': len(unique_ips_global),
            'total_visits': total_visits
        }
    })


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
    """View para página de certificados (Português)"""
    template_name = 'portfolio/certificados.html'
    
    def get_context_data(self, **kwargs):
        from .models import Certificate
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Certificados - Guilherme Nunes'
        context['language'] = 'pt'
        context['certificates'] = Certificate.objects.filter(is_active=True).order_by('-date_issued')
        return context


class CertificadosEnView(CertificadosView):
    """Certificates page (English)"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Certificates - Guilherme Nunes'
        context['language'] = 'en'
        return context


class CertificadosEsView(CertificadosView):
    """Página de certificados (Español)"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Certificados - Guilherme Nunes'
        context['language'] = 'es'
        return context


class RedesSociaisView(TemplateView):
    """View para página de redes sociais (Português)"""
    template_name = 'portfolio/redes_sociais.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Redes Sociais - Guilherme Nunes'
        context['language'] = 'pt'
        return context


class SocialEnView(TemplateView):
    """Social Media page (English)"""
    template_name = 'portfolio/redes_sociais.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Social Media - Guilherme Nunes'
        context['language'] = 'en'
        return context


class SocialEsView(TemplateView):
    """Página de redes sociales (Español)"""
    template_name = 'portfolio/redes_sociais.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Redes Sociales - Guilherme Nunes'
        context['language'] = 'es'
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
    from .models import Project, Certificate, Post, SiteConfig
    site_config = SiteConfig.load()
    stats = {
        'experience': '3+',
        'projects': Project.objects.filter(is_active=True).count(),
        'certifications': Certificate.objects.filter(is_active=True).count()
    }
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:2]
    return render(request, 'portfolio/home.html', {
        'language': 'pt',
        'page_title': f'Guilherme Nunes - {site_config.job_title_pt}',
        'stats': stats,
        'recent_posts': recent_posts,
        'site_config': site_config
    })


def home_en(request):
    """Home em inglês"""
    from .models import Project, Certificate, Post, SiteConfig
    site_config = SiteConfig.load()
    stats = {
        'experience': '3+',
        'projects': Project.objects.filter(is_active=True).count(),
        'certifications': Certificate.objects.filter(is_active=True).count()
    }
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:2]
    return render(request, 'portfolio/home_en.html', {
        'language': 'en',
        'page_title': f'Guilherme Nunes - {site_config.job_title_en}',
        'stats': stats,
        'recent_posts': recent_posts,
        'site_config': site_config
    })


def home_es(request):
    """Home em espanhol"""
    from .models import Project, Certificate, Post, SiteConfig
    site_config = SiteConfig.load()
    stats = {
        'experience': '3+',
        'projects': Project.objects.filter(is_active=True).count(),
        'certifications': Certificate.objects.filter(is_active=True).count()
    }
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:2]
    return render(request, 'portfolio/home_es.html', {
        'language': 'es',
        'page_title': f'Guilherme Nunes - {site_config.job_title_es}',
        'stats': stats,
        'recent_posts': recent_posts,
        'site_config': site_config
    })


class AboutView(TemplateView):
    """Página Sobre mim separada"""
    template_name = 'portfolio/sobre.html'

    def get_context_data(self, **kwargs):
        from .models import SiteConfig
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Sobre - Guilherme Nunes'
        context['language'] = 'pt'
        context['site_config'] = SiteConfig.load()
        return context


class AboutEnView(TemplateView):
    """English About page"""
    template_name = 'portfolio/about_en.html'

    def get_context_data(self, **kwargs):
        from .models import SiteConfig
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'About - Guilherme Nunes'
        context['language'] = 'en'
        context['site_config'] = SiteConfig.load()
        return context


class AboutEsView(TemplateView):
    """Spanish About page"""
    template_name = 'portfolio/about_es.html'

    def get_context_data(self, **kwargs):
        from .models import SiteConfig
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Sobre - Guilherme Nunes'
        context['language'] = 'es'
        context['site_config'] = SiteConfig.load()
        return context


class BlogView(ListView):
    """View para lista de posts do blog (Português)"""
    model = Post
    template_name = 'portfolio/blog.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = 'pt'
        context['page_title'] = 'Blog & Novidades - Guilherme Nunes'
        return context


class BlogEnView(BlogView):
    """Blog list (English)"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = 'en'
        context['page_title'] = 'Blog & News - Guilherme Nunes'
        return context


class BlogEsView(BlogView):
    """Lista de blog (Español)"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = 'es'
        context['page_title'] = 'Blog & Noticias - Guilherme Nunes'
        return context


class BlogDetailView(DetailView):
    """View para detalhes de um post do blog (Português)"""
    model = Post
    template_name = 'portfolio/blog_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = 'pt'
        context['page_title'] = f"{context['post'].title} - Guilherme Nunes"
        return context


class BlogDetailEnView(BlogDetailView):
    """Blog post detail (English)"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = 'en'
        context['page_title'] = f"{context['post'].title} - Guilherme Nunes"
        return context


class BlogDetailEsView(BlogDetailView):
    """Detalle del post (Español)"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = 'es'
        context['page_title'] = f"{context['post'].title} - Guilherme Nunes"
        return context


class VisitorMapView(TemplateView):
    """View para mapa de visitantes (Português)"""
    template_name = 'portfolio/mapa_visitantes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Mapa de Visitantes - Guilherme Nunes'
        context['language'] = 'pt'
        return context


class VisitorMapEnView(VisitorMapView):
    """Visitor map (English)"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Visitor Map - Guilherme Nunes'
        context['language'] = 'en'
        return context


class VisitorMapEsView(VisitorMapView):
    """Mapa de visitantes (Español)"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Mapa de Visitantes - Guilherme Nunes'
        context['language'] = 'es'
        return context


class CoursesView(ListView):
    """View para lista de cursos (Português)"""
    template_name = 'portfolio/cursos.html'
    context_object_name = 'courses'
    
    def get_queryset(self):
        from .models import Course
        qs = Course.objects.filter(is_active=True).prefetch_related('lessons')
        # Filtros
        order = self.request.GET.get('order')  # new|old
        category = self.request.GET.get('category')  # tag string
        if category and category != 'all':
            qs = qs.filter(tags__icontains=category)
        if order == 'old':
            qs = qs.order_by('created_at')
        else:  # default newest
            qs = qs.order_by('-created_at')
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Cursos - Guilherme Nunes'
        context['language'] = 'pt'
        # Categorias (tags) únicas
        all_tags = []
        for c in context['courses']:
            all_tags.extend(c.get_tags_list())
        context['categories'] = sorted(set([t for t in all_tags if t]))
        context['selected_category'] = self.request.GET.get('category', 'all')
        context['selected_order'] = self.request.GET.get('order', 'new')
        return context


class CoursesEnView(ListView):
    """View para lista de cursos (English)"""
    template_name = 'portfolio/cursos.html'
    context_object_name = 'courses'
    
    def get_queryset(self):
        from .models import Course
        qs = Course.objects.filter(is_active=True).prefetch_related('lessons')
        order = self.request.GET.get('order')
        category = self.request.GET.get('category')
        if category and category != 'all':
            qs = qs.filter(tags__icontains=category)
        if order == 'old':
            qs = qs.order_by('created_at')
        else:
            qs = qs.order_by('-created_at')
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Courses - Guilherme Nunes'
        context['language'] = 'en'
        all_tags = []
        for c in context['courses']:
            all_tags.extend(c.get_tags_list())
        context['categories'] = sorted(set([t for t in all_tags if t]))
        context['selected_category'] = self.request.GET.get('category', 'all')
        context['selected_order'] = self.request.GET.get('order', 'new')
        return context


class CoursesEsView(ListView):
    """View para lista de cursos (Español)"""
    template_name = 'portfolio/cursos.html'
    context_object_name = 'courses'
    
    def get_queryset(self):
        from .models import Course
        qs = Course.objects.filter(is_active=True).prefetch_related('lessons')
        order = self.request.GET.get('order')
        category = self.request.GET.get('category')
        if category and category != 'all':
            qs = qs.filter(tags__icontains=category)
        if order == 'old':
            qs = qs.order_by('created_at')
        else:
            qs = qs.order_by('-created_at')
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Cursos - Guilherme Nunes'
        context['language'] = 'es'
        all_tags = []
        for c in context['courses']:
            all_tags.extend(c.get_tags_list())
        context['categories'] = sorted(set([t for t in all_tags if t]))
        context['selected_category'] = self.request.GET.get('category', 'all')
        context['selected_order'] = self.request.GET.get('order', 'new')
        return context


class CourseDetailView(DetailView):
    """View para detalhes de um curso com suas aulas"""
    template_name = 'portfolio/curso_detail.html'
    context_object_name = 'course'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        from .models import Course
        return Course.objects.filter(is_active=True).prefetch_related('lessons')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.object.lessons.filter(is_active=True)
        context['page_title'] = f'{self.object.title} - Guilherme Nunes'
        path = self.request.path
        if path.startswith('/en/'):  # /en/courses/slug/
            context['language'] = 'en'
        elif path.startswith('/es/'):  # /es/cursos/slug/
            context['language'] = 'es'
        else:
            context['language'] = 'pt'
        return context