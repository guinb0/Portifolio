"""
Middleware para rastreamento de visitantes
"""
import requests
from .models import Visitor
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class VisitorTrackingMiddleware:
    """
    Middleware para rastrear visitantes e suas localizações
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Ignora requisições para arquivos estáticos, admin e API
        if (request.path.startswith('/static/') or 
            request.path.startswith('/admin/') or
            request.path.startswith('/api/')):
            return self.get_response(request)
        
        # Obtém o IP do visitante
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
        
        # User agent
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        try:
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
                    # Se falhar, não registra IPs locais
                    return self.get_response(request)
            
            # Verifica se o visitante já existe
            try:
                visitor = Visitor.objects.get(ip_address=ip)
                # Atualiza última visita e contador
                visitor.visit_count += 1
                visitor.last_visit = timezone.now()
                visitor.user_agent = user_agent
                visitor.save()
                logger.info(f'Visitante atualizado: {ip} - Visita #{visitor.visit_count}')
                
            except Visitor.DoesNotExist:
                # Novo visitante - busca geolocalização
                try:
                    response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('status') == 'success':
                            visitor = Visitor.objects.create(
                                ip_address=ip,
                                country=data.get('country', 'Desconhecido'),
                                country_code=data.get('countryCode', ''),
                                region=data.get('regionName', ''),
                                city=data.get('city', 'Desconhecido'),
                                latitude=data.get('lat', 0),
                                longitude=data.get('lon', 0),
                                user_agent=user_agent,
                                visit_count=1
                            )
                            logger.info(f'Novo visitante registrado: {ip} - {data.get("city")}, {data.get("country")}')
                        else:
                            # API retornou erro, registra sem geolocalização
                            visitor = Visitor.objects.create(
                                ip_address=ip,
                                country='Desconhecido',
                                city='Desconhecido',
                                user_agent=user_agent,
                                visit_count=1
                            )
                            logger.warning(f'Visitante registrado sem geolocalização: {ip}')
                    else:
                        # Falha na API, registra sem geo
                        visitor = Visitor.objects.create(
                            ip_address=ip,
                            country='Desconhecido',
                            city='Desconhecido',
                            user_agent=user_agent,
                            visit_count=1
                        )
                        logger.warning(f'Visitante registrado sem geolocalização: {ip}')
                        
                except requests.RequestException as e:
                    # Se houver erro na API, ainda registra o visitante sem geolocalização
                    visitor = Visitor.objects.create(
                        ip_address=ip,
                        country='Desconhecido',
                        city='Desconhecido',
                        user_agent=user_agent,
                        visit_count=1
                    )
                    logger.error(f'Erro ao obter geolocalização para {ip}: {e}')
                    
        except Exception as e:
            logger.error(f'Erro no middleware de visitantes: {e}')
        
        response = self.get_response(request)
        return response