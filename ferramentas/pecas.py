"""Peças estáticas (feed 4:5 e stories 9:16) a partir de HTML. Uso: from pecas import render; render({nome: html}, pasta)."""
from playwright.sync_api import sync_playwright

from estilo import pagina


def render(pecas, pasta):
    import os
    pasta = os.path.abspath(pasta)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 1100, "height": 2000})
        for nome, corpo in pecas.items():
            open(f"{pasta}/_t.html", "w").write(pagina(corpo))
            pg.goto(f"file://{pasta}/_t.html"); pg.wait_for_timeout(250)
            pg.locator(".peca").screenshot(path=f"{pasta}/{nome}.jpg", type="jpeg", quality=92)
        br.close()
