"""Build static site for GitHub Pages deployment."""

import shutil
from pathlib import Path

from app import app

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()

    shutil.copytree(ROOT / "static", DOCS / "static")

    with app.test_client() as client:
        html = client.get("/").data.decode("utf-8")

    # Use relative asset paths for GitHub project pages (/Portifolio/).
    html = html.replace('="/static/', '="static/')
    html = html.replace("='/static/", "='static/")
    html = html.replace('href="/certificados"', 'href="index.html"')

    (DOCS / "index.html").write_text(html, encoding="utf-8")
    print(f"Static site built at {DOCS}")


if __name__ == "__main__":
    main()
