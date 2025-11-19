# 🚀 Guia de Início Rápido

## ⚡ Instalação em 5 Minutos

### 1️⃣ Extrair o projeto
```bash
unzip portfolio_django.zip
cd portfolio_django
```

### 2️⃣ Criar ambiente virtual
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar banco de dados
```bash
python manage.py migrate
```

### 5️⃣ Criar superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 6️⃣ Rodar servidor
```bash
python manage.py runserver
```

### 7️⃣ Acessar o site
Abra seu navegador em: `http://127.0.0.1:8000/`

---

## 🎨 Primeira Personalização

### Mudar Cores do Site

Edite `static/css/base.css`:
```css
:root {
    --primary-color: #SUA-COR;
    --secondary-color: #SUA-COR;
}
```

### Mudar Informações Pessoais

Edite `templates/portfolio/sections/_home.html`:
```html
<h1>SEU NOME</h1>
<h2>SUA PROFISSÃO</h2>
<p>Sua descrição...</p>
```

### Adicionar seus Links

Edite `templates/portfolio/sections/_contact.html`:
```html
<p>Sua localização</p>
<p>Seu telefone</p>
<p>Seu email</p>
```

---

## 📁 Adicionar suas Imagens

Coloque suas imagens em `static/img/`:
- `Foto3.png` - Foto principal (home)
- `IMG_2024_07_04_175231.png` - Foto about
- Outras imagens de projetos

---

## 🎯 Próximos Passos

1. ✅ Personalize as cores
2. ✅ Adicione suas informações
3. ✅ Coloque suas fotos
4. ✅ Adicione seus projetos
5. ✅ Configure o admin Django
6. ✅ Teste o dark mode
7. ✅ Teste a responsividade

---

## 📚 Documentação Completa

- **README.md** - Documentação completa do projeto
- **ARQUITETURA.md** - Explicação da arquitetura modular
- **COMANDOS.md** - Lista de comandos úteis do Django

---

## 🆘 Problemas Comuns

### Erro: "No module named 'django'"
```bash
pip install Django
```

### Erro: "Port already in use"
```bash
python manage.py runserver 8080
```

### Erro: "Static files not found"
```bash
python manage.py collectstatic
```

---

## 🎉 Pronto!

Seu portfolio Django está funcionando!

Explore os arquivos e comece a personalizar! 🚀
