# Portfolio Django - Guilherme Nunes

Portfolio profissional migrado de Flask para Django com arquitetura modular e fácil manutenção.

## 🎯 Características

- **Arquitetura Modular**: CSS, JavaScript e Templates divididos em seções independentes
- **Dark Mode**: Tema escuro/claro com persistência no localStorage
- **Responsivo**: Design adaptável para desktop, tablet e mobile
- **Animações**: ScrollReveal e animações CSS suaves
- **Internacionalização**: Suporte para PT, EN e ES
- **Admin Django**: Gerenciamento fácil de projetos, certificados e serviços
- **SEO Friendly**: Estrutura otimizada para motores de busca

## 📁 Estrutura do Projeto

```
portfolio_django/
├── config/                  # Configurações do Django
│   ├── __init__.py
│   ├── settings.py         # Configurações principais
│   ├── urls.py             # URLs principais
│   └── wsgi.py             # WSGI config
│
├── portfolio/              # App principal
│   ├── migrations/         # Migrações do banco
│   ├── __init__.py
│   ├── admin.py           # Configuração do Admin
│   ├── apps.py            # Config da app
│   ├── models.py          # Models (Project, Certificate, etc)
│   ├── urls.py            # URLs da app
│   └── views.py           # Views
│
├── templates/
│   └── portfolio/
│       ├── base.html                # Template base
│       ├── home.html               # Template principal
│       ├── partials/
│       │   └── _header.html       # Header reutilizável
│       └── sections/
│           ├── _home.html         # Seção home
│           ├── _stats.html        # Seção estatísticas
│           ├── _about.html        # Seção sobre
│           ├── _services.html     # Seção serviços
│           ├── _portfolio.html    # Seção projetos
│           └── _contact.html      # Seção contato
│
├── static/
│   ├── css/
│   │   ├── base.css              # Estilos globais e variáveis
│   │   ├── header.css            # Estilos do header
│   │   ├── home.css              # Estilos home e stats
│   │   ├── about.css             # Estilos about
│   │   ├── services.css          # Estilos services
│   │   ├── portfolio.css         # Estilos portfolio
│   │   ├── contact.css           # Estilos contact
│   │   └── responsive.css        # Media queries
│   │
│   ├── js/
│   │   ├── theme-toggle.js       # Toggle dark mode
│   │   ├── menu-mobile.js        # Menu responsivo
│   │   ├── scroll-reveal.js      # Animações scroll
│   │   └── stats-animation.js    # Animação números
│   │
│   └── img/                      # Imagens do site
│
├── manage.py
└── requirements.txt
```

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone <seu-repositorio>
cd portfolio_django
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 6. Colete arquivos estáticos
```bash
python manage.py collectstatic --noinput
```

### 7. Execute o servidor
```bash
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/`

## 🎨 Estrutura de Templates

### Template Base (`base.html`)
Contém a estrutura HTML comum a todas as páginas:
- `<head>` com meta tags e links CSS
- Header (incluído via partial)
- Bloco de conteúdo
- Scripts JavaScript

### Seções Modulares
Cada seção é um arquivo separado em `templates/portfolio/sections/`:

- **`_home.html`**: Hero section com foto e call-to-action
- **`_stats.html`**: Estatísticas animadas
- **`_about.html`**: Sobre mim com foto e redes sociais
- **`_services.html`**: Serviços oferecidos
- **`_portfolio.html`**: Galeria de projetos
- **`_contact.html`**: Informações de contato

### Como usar as seções
No template principal (`home.html`):
```django
{% extends 'portfolio/base.html' %}

{% block content %}
    {% include 'portfolio/sections/_home.html' %}
    {% include 'portfolio/sections/_stats.html' %}
    {% include 'portfolio/sections/_about.html' %}
    {% include 'portfolio/sections/_services.html' %}
    {% include 'portfolio/sections/_portfolio.html' %}
    {% include 'portfolio/sections/_contact.html' %}
{% endblock %}
```

## 🎨 Estrutura de CSS

### CSS Modular
Cada seção tem seu próprio arquivo CSS:

- **`base.css`**: Variáveis CSS, reset, estilos globais
- **`header.css`**: Navegação, logo, menu mobile, theme toggle
- **`home.css`**: Hero section e estatísticas
- **`about.css`**: Seção sobre
- **`services.css`**: Cards de serviços
- **`portfolio.css`**: Galeria de projetos
- **`contact.css`**: Seção de contato
- **`responsive.css`**: Media queries para todos os breakpoints

### Variáveis CSS
Definidas em `base.css`:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --text-dark: #1a202c;
    --text-light: #718096;
    --bg-light: #f7fafc;
    --bg-white: #ffffff;
    --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    /* ... */
}
```

### Dark Mode
Variáveis sobrescritas automaticamente:
```css
body.dark {
    --text-dark: #f7fafc;
    --text-light: #cbd5e0;
    --bg-light: #1a202c;
    --bg-white: #2d3748;
}
```

## 📱 JavaScript Modular

### Arquivos JavaScript
- **`theme-toggle.js`**: Toggle entre light/dark mode
- **`menu-mobile.js`**: Funcionalidade do menu hambúrguer
- **`scroll-reveal.js`**: Animações ao rolar a página
- **`stats-animation.js`**: Animação dos números das estatísticas

### Carregamento
Todos os scripts são carregados no final do `base.html`:
```html
<script src="{% static 'js/theme-toggle.js' %}"></script>
<script src="{% static 'js/menu-mobile.js' %}"></script>
<script src="{% static 'js/scroll-reveal.js' %}"></script>
<script src="{% static 'js/stats-animation.js' %}"></script>
```

## 🗄️ Models Django

### Project
```python
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    tags = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
```

### Certificate
```python
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    image = models.ImageField(upload_to='certificates/')
    date_issued = models.DateField()
    is_active = models.BooleanField(default=True)
```

### Service
```python
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100)  # classe boxicons
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
```

## 🔧 Admin Django

Acesse `/admin` para gerenciar:
- Projetos do portfolio
- Certificados
- Serviços oferecidos
- Mensagens de contato

## 🌐 Internacionalização

### URLs disponíveis:
- `/` - Português (padrão)
- `/EN/` - English
- `/ES/` - Español

### Adicionar novo idioma:
1. Crie o template: `templates/portfolio/home_fr.html`
2. Adicione a view em `portfolio/views.py`
3. Adicione a URL em `portfolio/urls.py`
4. Adicione a bandeira no dropdown do header

## 📝 Customização

### Alterar cores
Edite as variáveis em `static/css/base.css`:
```css
:root {
    --primary-color: #sua-cor-aqui;
    --secondary-color: #sua-cor-aqui;
    /* ... */
}
```

### Adicionar nova seção
1. Crie o template: `templates/portfolio/sections/_nova_secao.html`
2. Crie o CSS: `static/css/nova-secao.css`
3. Inclua o CSS no `base.html`
4. Inclua a seção no `home.html`

### Modificar animações
Edite `static/js/scroll-reveal.js`:
```javascript
ScrollReveal().reveal('.sua-classe', { 
    origin: 'bottom',
    distance: '80px',
    duration: 2000
});
```

## 🚀 Deploy

### Preparação
1. Configure `DEBUG = False` em `settings.py`
2. Adicione seu domínio em `ALLOWED_HOSTS`
3. Configure `SECRET_KEY` segura
4. Configure banco de dados de produção

### Heroku
```bash
# Criar Procfile
echo "web: gunicorn config.wsgi" > Procfile

# Instalar gunicorn
pip install gunicorn
pip freeze > requirements.txt

# Deploy
heroku create seu-app
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Arquivos estáticos
```bash
python manage.py collectstatic --noinput
```

## 📄 Licença

Este projeto está sob a licença MIT.

## 👤 Autor

**Guilherme Nunes**
- GitHub: [@guinb0](https://github.com/guinb0)
- LinkedIn: [guinb](https://www.linkedin.com/in/guinb/)
- Email: guilhermenunesfev26@gmail.com

---

Desenvolvido com ❤️ usando Django
