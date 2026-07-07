"""
Portfólio — Guilherme Nunes Bezerra (Full Stack Developer)
Aplicação Flask.

Como rodar:
    pip install -r requirements.txt
    python app.py
Depois abra http://127.0.0.1:5000

Estrutura esperada:
    app.py
    templates/
        index.html
        navbar.html
        home.html
    static/
        css/  (style.css, navbar.css, home.css)
        js/   (main.js)
        img/  (fotos, projetos, bandeiras)
"""

from flask import Flask, render_template

app = Flask(__name__)


# --- Página principal (Português) ---
@app.route("/")
def index():
    return render_template("index.html")


# --- Versões de idioma ---
# Enquanto não houver templates dedicados (index_en.html / index_es.html),
# ambas caem na página principal. Basta criar os templates e trocar aqui.
@app.route("/EN")
def index_en():
    return render_template("index.html")


@app.route("/ES")
def index_es():
    return render_template("index.html")


# --- Outras páginas ---
@app.route("/certificados")
def certificados():
    # Troque por render_template("certificados.html") quando o template existir.
    return render_template("index.html")


@app.route("/redes")
def redes():
    return render_template("index.html")


@app.route("/receitas")
def receitas():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
