# 🌍 Configuração da Tela de Seleção de Idioma

## ✅ Arquivos Criados

1. **Template**: `templates/portfolio/language_selector.html`
2. **CSS**: `static/css/language-selector.css`
3. **Pasta para bandeiras**: `static/images/flags/`

## 📋 O Que Fazer Agora

### 1. Adicionar as Imagens das Bandeiras

Coloque as seguintes imagens na pasta `static/images/flags/`:

- **brazil.png** - Bandeira do Brasil 🇧🇷
- **usa.png** - Bandeira dos EUA 🇺🇸
- **spain.png** - Bandeira da Espanha 🇪🇸

**Especificações recomendadas:**
- Formato: PNG (com ou sem fundo transparente)
- Tamanho: 120x120px ou maior
- As imagens serão redimensionadas e exibidas em círculos

### 2. Onde Encontrar Bandeiras (Grátis)

**Opção 1 - Flaticon (Recomendado):**
- Acesse: https://www.flaticon.com/search?word=flags
- Busque por "brazil flag", "usa flag", "spain flag"
- Escolha o estilo circular ou quadrado
- Baixe em PNG

**Opção 2 - Freepik:**
- Acesse: https://www.freepik.com/search?format=search&query=country%20flags
- Filtros: PNG, alta resolução

**Opção 3 - Wikimedia Commons (Domínio Público):**
- Acesse: https://commons.wikimedia.org/wiki/Category:National_flags
- Totalmente gratuito

**Opção 4 - Font Awesome (Usar emojis de bandeira):**
Se preferir não usar imagens, pode usar emojis Unicode:
- Brasil: 🇧🇷
- EUA: 🇺🇸
- Espanha: 🇪🇸

## 🚀 Como Funciona

### Fluxo de Navegação:

1. **Primeira tela (/)**: Seleção de idioma com 3 bandeiras
2. **Português (/pt/)**: Portfolio em português
3. **English (/en/)**: Portfolio em inglês
4. **Español (/es/)**: Portfolio em espanhol

### URLs Atualizadas:

```
/           → Seleção de idioma (NEW!)
/pt/        → Home em português
/en/        → Home em inglês
/es/        → Home em espanhol
```

## 🎨 Design da Tela

A tela de seleção possui:
- ✨ Fundo gradiente (roxo/azul)
- 🎴 3 cards com bandeiras circulares
- 🖱️ Efeito hover (cards sobem ao passar o mouse)
- 📱 Totalmente responsivo
- 🌈 Animação suave ao carregar

## 🧪 Para Testar

1. Adicione as 3 imagens das bandeiras na pasta `static/images/flags/`
2. Reinicie o servidor Django (se necessário)
3. Acesse: http://127.0.0.1:8000/
4. Você verá a tela de seleção de idioma!

## 🔄 Alternativa Sem Imagens (Temporário)

Se quiser testar antes de adicionar as bandeiras, você pode usar emojis. 
Edite o arquivo `language_selector.html` e substitua as tags `<img>` por:

```html
<div class="flag-emoji">🇧🇷</div>  <!-- Brasil -->
<div class="flag-emoji">🇺🇸</div>  <!-- EUA -->
<div class="flag-emoji">🇪🇸</div>  <!-- Espanha -->
```

E adicione este CSS em `language-selector.css`:

```css
.flag-emoji {
    font-size: 80px;
}
```

## 📝 Observações

- As bandeiras devem ter os nomes exatos: `brazil.png`, `usa.png`, `spain.png`
- Você pode trocar para `.jpg` se preferir (lembre de atualizar no HTML)
- O design funciona bem com bandeiras circulares ou quadradas
