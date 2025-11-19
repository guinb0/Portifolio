"""
Middleware para rastreamento de visitantes
"""
import requests
from .models import Visitor
import logging

logger = logging.getLogger(__name__)


class VisitorTrackingMiddleware:
    """
    Middleware para rastrear visitantes e suas localizações
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Ignora requisições para arquivos estáticos e admin
        if request.path.startswith('/static/') or request.path.startswith('/admin/'):
            return self.get_response(request)
        
        # Obtém o IP do visitante
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
        
        # User agent
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        # Verifica se este IP já foi registrado recentemente (nas últimas 24 horas)
        from django.utils import timezone
        from datetime import timedelta
        
        try:
            recent_visit = Visitor.objects.filter(
                ip_address=ip,
                visited_at__gte=timezone.now() - timedelta(hours=24)
            ).exists()
            
            # Se não há visita recente, registra nova visita
            if not recent_visit:
                # Para localhost/desenvolvimento, tenta obter IP público real
                if ip in ['127.0.0.1', 'localhost', '::1']:
                    try:
                        # Obtém o IP público real do usuário
                        public_ip_response = requests.get('https://api.ipify.org?format=json', timeout=3)
                        if public_ip_response.status_code == 200:
                            real_ip = public_ip_response.json().get('ip')
                            if real_ip:
                                ip = real_ip
                                logger.info(f'IP público detectado: {ip}')
                    except Exception as e:
                        logger.warning(f'Não foi possível obter IP público: {e}')
                
                try:
                    # Tenta obter geolocalização usando API gratuita
                    response = requests.get(f'http://ip-api.com/json/{ip}', timeout=3)
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('status') == 'success':
                            Visitor.objects.create(
                                ip_address=ip,
                                country=data.get('country', ''),
                                country_code=data.get('countryCode', ''),
                                region=data.get('regionName', ''),
                                city=data.get('city', ''),
                                latitude=data.get('lat'),
                                longitude=data.get('lon'),
                                user_agent=user_agent
                            )
                            logger.info(f'Visitante registrado: {ip} - {data.get("city")}, {data.get("country")}')
                        else:
                            # API retornou erro, registra sem geolocalização
                            Visitor.objects.create(
                                ip_address=ip,
                                user_agent=user_agent
                            )
                            logger.warning(f'Visitante registrado sem geolocalização: {ip}')
                except requests.RequestException as e:
                    # Se houver erro na API, ainda registra o visitante sem geolocalização
                    Visitor.objects.create(
                        ip_address=ip,
                        user_agent=user_agent
                    )
                    logger.error(f'Erro ao obter geolocalização para {ip}: {e}')
        except Exception as e:
            logger.error(f'Erro no middleware de visitantes: {e}')
        
        response = self.get_response(request)
        return response
