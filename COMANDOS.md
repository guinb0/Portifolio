# Guia Rápido de Comandos Django

## 🚀 Comandos Básicos

### Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Migrations
```bash
# Criar migrations
python manage.py makemigrations

# Aplicar migrations
python manage.py migrate

# Ver SQL das migrations
python manage.py sqlmigrate portfolio 0001

# Mostrar migrations
python manage.py showmigrations
```

### Servidor de Desenvolvimento
```bash
# Rodar servidor
python manage.py runserver

# Rodar em porta específica
python manage.py runserver 8080

# Rodar em IP específico
python manage.py runserver 0.0.0.0:8000
```

### Admin
```bash
# Criar superusuário
python manage.py createsuperuser

# Mudar senha de usuário
python manage.py changepassword username
```

### Arquivos Estáticos
```bash
# Coletar arquivos estáticos
python manage.py collectstatic

# Limpar e coletar novamente
python manage.py collectstatic --clear --noinput
```

### Shell Django
```bash
# Abrir shell
python manage.py shell

# Shell com IPython
python manage.py shell -i ipython
```

### Testes
```bash
# Rodar todos os testes
python manage.py test

# Rodar testes de uma app
python manage.py test portfolio

# Rodar teste específico
python manage.py test portfolio.tests.ProjectModelTestCase

# Rodar com coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

### Database
```bash
# Fazer backup do banco (SQLite)
python manage.py dumpdata > backup.json

# Restaurar backup
python manage.py loaddata backup.json

# Limpar banco de dados
python manage.py flush

# Dump de uma app específica
python manage.py dumpdata portfolio > portfolio_backup.json
```

### Gerenciamento
```bash
# Verificar problemas no projeto
python manage.py check

# Limpar sessões expiradas
python manage.py clearsessions

# Ver todas as URLs do projeto
python manage.py show_urls  # requer django-extensions
```

## 📝 Comandos Úteis do Git

```bash
# Inicializar repositório
git init

# Adicionar arquivos
git add .

# Commit
git commit -m "Mensagem do commit"

# Push
git push origin main

# Pull
git pull origin main

# Ver status
git status

# Ver histórico
git log --oneline
```

## 🔧 Comandos de Manutenção

### Atualizar dependências
```bash
pip list --outdated
pip install --upgrade package-name
pip freeze > requirements.txt
```

### Limpar arquivos Python compilados
```bash
find . -type f -name "*.py[co]" -delete
find . -type d -name "__pycache__" -delete
```

### Verificar código
```bash
# Com flake8
flake8 .

# Com pylint
pylint portfolio/

# Com black (formatação)
black .

# Com isort (imports)
isort .
```

## 📊 Performance e Debug

```bash
# Debug toolbar (adicionar ao settings)
pip install django-debug-toolbar

# Analisar queries
python manage.py debugsqlshell

# Ver queries lentas
python manage.py shell
from django.db import connection
print(connection.queries)
```

## 🚀 Deploy

### Heroku
```bash
# Login
heroku login

# Criar app
heroku create nome-do-app

# Configurar variáveis de ambiente
heroku config:set SECRET_KEY="sua-secret-key"
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Migrations no Heroku
heroku run python manage.py migrate

# Criar superusuário no Heroku
heroku run python manage.py createsuperuser

# Ver logs
heroku logs --tail

# Abrir app
heroku open
```

### Comandos Personalizados

Para criar seus próprios comandos Django:

1. Crie a estrutura:
```
portfolio/
  management/
    __init__.py
    commands/
      __init__.py
      seu_comando.py
```

2. Exemplo de comando (`seu_comando.py`):
```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Descrição do seu comando'

    def handle(self, *args, **options):
        self.stdout.write('Seu código aqui')
```

3. Executar:
```bash
python manage.py seu_comando
```

## 💡 Dicas

- Use `python manage.py help` para ver todos os comandos disponíveis
- Use `python manage.py help comando` para ver ajuda de um comando específico
- Use `--settings` para usar arquivo de settings diferente
- Use `--verbosity` para controlar nível de output (0-3)
- Use `--no-color` para desabilitar cores no output
