"""
Comando para popular o banco de dados com visitantes de teste
"""
from django.core.management.base import BaseCommand
from portfolio.models import Visitor


class Command(BaseCommand):
    help = 'Adiciona visitantes de exemplo ao banco de dados'

    def handle(self, *args, **options):
        # Lista de visitantes de exemplo de diferentes locais do mundo
        sample_visitors = [
            {
                'ip_address': '192.168.1.100',
                'country': 'Brasil',
                'country_code': 'BR',
                'region': 'São Paulo',
                'city': 'São Paulo',
                'latitude': -23.5505,
                'longitude': -46.6333,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            },
            {
                'ip_address': '192.168.1.101',
                'country': 'Brasil',
                'country_code': 'BR',
                'region': 'Rio de Janeiro',
                'city': 'Rio de Janeiro',
                'latitude': -22.9068,
                'longitude': -43.1729,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            },
            {
                'ip_address': '192.168.1.102',
                'country': 'Estados Unidos',
                'country_code': 'US',
                'region': 'California',
                'city': 'San Francisco',
                'latitude': 37.7749,
                'longitude': -122.4194,
                'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
            },
            {
                'ip_address': '192.168.1.103',
                'country': 'Estados Unidos',
                'country_code': 'US',
                'region': 'New York',
                'city': 'New York',
                'latitude': 40.7128,
                'longitude': -74.0060,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            },
            {
                'ip_address': '192.168.1.104',
                'country': 'Reino Unido',
                'country_code': 'GB',
                'region': 'England',
                'city': 'London',
                'latitude': 51.5074,
                'longitude': -0.1278,
                'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
            },
            {
                'ip_address': '192.168.1.105',
                'country': 'Alemanha',
                'country_code': 'DE',
                'region': 'Berlin',
                'city': 'Berlin',
                'latitude': 52.5200,
                'longitude': 13.4050,
                'user_agent': 'Mozilla/5.0 (X11; Linux x86_64)'
            },
            {
                'ip_address': '192.168.1.106',
                'country': 'França',
                'country_code': 'FR',
                'region': 'Île-de-France',
                'city': 'Paris',
                'latitude': 48.8566,
                'longitude': 2.3522,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            },
            {
                'ip_address': '192.168.1.107',
                'country': 'Japão',
                'country_code': 'JP',
                'region': 'Tokyo',
                'city': 'Tokyo',
                'latitude': 35.6762,
                'longitude': 139.6503,
                'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
            },
            {
                'ip_address': '192.168.1.108',
                'country': 'Austrália',
                'country_code': 'AU',
                'region': 'New South Wales',
                'city': 'Sydney',
                'latitude': -33.8688,
                'longitude': 151.2093,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            },
            {
                'ip_address': '192.168.1.109',
                'country': 'Canadá',
                'country_code': 'CA',
                'region': 'Ontario',
                'city': 'Toronto',
                'latitude': 43.6532,
                'longitude': -79.3832,
                'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
            },
            {
                'ip_address': '192.168.1.110',
                'country': 'Espanha',
                'country_code': 'ES',
                'region': 'Madrid',
                'city': 'Madrid',
                'latitude': 40.4168,
                'longitude': -3.7038,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            },
            {
                'ip_address': '192.168.1.111',
                'country': 'Itália',
                'country_code': 'IT',
                'region': 'Lazio',
                'city': 'Roma',
                'latitude': 41.9028,
                'longitude': 12.4964,
                'user_agent': 'Mozilla/5.0 (X11; Linux x86_64)'
            },
            {
                'ip_address': '192.168.1.112',
                'country': 'Brasil',
                'country_code': 'BR',
                'region': 'Minas Gerais',
                'city': 'Belo Horizonte',
                'latitude': -19.9167,
                'longitude': -43.9345,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            },
            {
                'ip_address': '192.168.1.113',
                'country': 'Argentina',
                'country_code': 'AR',
                'region': 'Buenos Aires',
                'city': 'Buenos Aires',
                'latitude': -34.6037,
                'longitude': -58.3816,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            },
            {
                'ip_address': '192.168.1.114',
                'country': 'México',
                'country_code': 'MX',
                'region': 'Ciudad de México',
                'city': 'Ciudad de México',
                'latitude': 19.4326,
                'longitude': -99.1332,
                'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
            },
        ]

        created_count = 0
        for visitor_data in sample_visitors:
            # Verifica se já existe
            if not Visitor.objects.filter(ip_address=visitor_data['ip_address']).exists():
                Visitor.objects.create(**visitor_data)
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"✓ Criado: {visitor_data['city']}, {visitor_data['country']}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n{created_count} visitante(s) adicionado(s) com sucesso!'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'Total de visitantes no banco: {Visitor.objects.count()}'
            )
        )
