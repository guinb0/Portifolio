"""
Testes para a app portfolio
"""
from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Project, Certificate, Service


class ViewsTestCase(TestCase):
    """Testes para as views"""
    
    def setUp(self):
        self.client = Client()
    
    def test_home_view(self):
        """Testa se a home page carrega"""
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/home.html')
    
    def test_home_en_view(self):
        """Testa se a home em inglês carrega"""
        response = self.client.get(reverse('portfolio:home_en'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_es_view(self):
        """Testa se a home em espanhol carrega"""
        response = self.client.get(reverse('portfolio:home_es'))
        self.assertEqual(response.status_code, 200)


class ProjectModelTestCase(TestCase):
    """Testes para o model Project"""
    
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='Test Description',
            tags='python,django,test',
            order=1,
            is_active=True
        )
    
    def test_project_creation(self):
        """Testa criação de projeto"""
        self.assertEqual(self.project.title, 'Test Project')
        self.assertTrue(self.project.is_active)
    
    def test_get_tags_list(self):
        """Testa método get_tags_list"""
        tags = self.project.get_tags_list()
        self.assertEqual(len(tags), 3)
        self.assertIn('python', tags)
        self.assertIn('django', tags)
    
    def test_project_str(self):
        """Testa método __str__"""
        self.assertEqual(str(self.project), 'Test Project')


class CertificateModelTestCase(TestCase):
    """Testes para o model Certificate"""
    
    def setUp(self):
        from datetime import date
        self.certificate = Certificate.objects.create(
            title='Test Certificate',
            institution='Test Institution',
            description='Test Description',
            date_issued=date.today(),
            is_active=True
        )
    
    def test_certificate_creation(self):
        """Testa criação de certificado"""
        self.assertEqual(self.certificate.title, 'Test Certificate')
        self.assertEqual(self.certificate.institution, 'Test Institution')
        self.assertTrue(self.certificate.is_active)
    
    def test_certificate_str(self):
        """Testa método __str__"""
        expected = f"{self.certificate.title} - {self.certificate.institution}"
        self.assertEqual(str(self.certificate), expected)


class ServiceModelTestCase(TestCase):
    """Testes para o model Service"""
    
    def setUp(self):
        self.service = Service.objects.create(
            title='Test Service',
            description='Test Description',
            icon='bx-data',
            order=1,
            is_active=True
        )
    
    def test_service_creation(self):
        """Testa criação de serviço"""
        self.assertEqual(self.service.title, 'Test Service')
        self.assertEqual(self.service.icon, 'bx-data')
        self.assertTrue(self.service.is_active)
    
    def test_service_str(self):
        """Testa método __str__"""
        self.assertEqual(str(self.service), 'Test Service')
