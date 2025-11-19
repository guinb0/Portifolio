"""
Views para o portfolio
"""
from django.shortcuts import render
from django.views.generic import TemplateView


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
