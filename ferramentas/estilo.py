"""Estilo comum das artes do Instagram @eonsistema."""
import html
import os
import sys

from playwright.sync_api import sync_playwright

E = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")  # fonte, logo, mascote e telas

LOGO = open(f"{E}/img/eon.svg").read().split("?>")[-1]
CSS = f"""
@font-face{{font-family:J;src:url(file://{E}/fonts/plus-jakarta-sans-latin-wght-normal.woff2) format('woff2');font-weight:200 800}}
@font-face{{font-family:J;src:url(file://{E}/fonts/plus-jakarta-sans-latin-ext-wght-normal.woff2) format('woff2');font-weight:200 800;unicode-range:U+0100-024F}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:J,sans-serif;background:#fff}}
.peca{{position:relative;overflow:hidden;color:#fff;background:radial-gradient(120% 90% at 85% 75%,#1d4a7d 0%,#0f2a4a 55%,#0b1f38 100%)}}
.f{{width:1080px;height:1350px;padding:96px 88px}}
.s{{width:1080px;height:1920px;padding:150px 88px}}
.marca{{display:flex;align-items:center;gap:18px;font-weight:800;font-size:40px;letter-spacing:.5px;color:#7be0a6}}
.marca svg{{width:64px;height:64px}}
h1{{font-weight:800;font-size:92px;line-height:1.04;letter-spacing:-2px;margin-top:56px}}
h1 em,h2 em{{font-style:normal;color:#7be0a6}}
h2{{font-weight:800;font-size:76px;line-height:1.06;letter-spacing:-1.5px;margin-top:40px}}
p.l{{font-size:38px;line-height:1.4;color:#c9d6e6;margin-top:32px;font-weight:500}}
.tag{{display:inline-block;background:#7be0a6;color:#0b2a1b;font-weight:800;font-size:28px;padding:12px 26px;border-radius:999px;letter-spacing:.5px;text-transform:uppercase}}
.rod{{position:absolute;left:88px;right:88px;bottom:72px;display:flex;justify-content:space-between;font-size:26px;color:#93a8c2;font-weight:600}}
.num{{position:absolute;right:88px;top:104px;font-size:28px;font-weight:700;color:#93a8c2}}
.tela{{position:absolute;left:56px;right:56px;bottom:118px;border-radius:28px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.45)}}
.tela img{{width:100%;display:block}}
.masc{{position:absolute;right:30px;bottom:110px;width:520px}}
.cta{{margin-top:56px;display:inline-flex;align-items:center;gap:16px;background:#0b7f4f;color:#fff;font-weight:800;font-size:40px;padding:28px 44px;border-radius:22px}}
ul.k{{list-style:none;margin-top:52px}}
ul.k li{{font-size:40px;font-weight:600;padding:24px 0 24px 72px;position:relative;border-bottom:2px solid rgba(255,255,255,.1)}}
ul.k li:before{{content:"";position:absolute;left:0;top:28px;width:44px;height:44px;border-radius:12px;background:#7be0a6 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230b2a1b' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5'/%3E%3C/svg%3E") center/30px no-repeat}}
.linha{{margin-top:60px;border-left:6px solid #7be0a6;padding-left:40px}}
.linha div{{margin-bottom:70px}}
.linha b{{display:block;font-size:44px;color:#7be0a6;font-weight:800}}
.linha span{{font-size:52px;font-weight:700;line-height:1.3}}
.caixa{{background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.12);border-radius:32px;padding:48px}}
"""
MARCA = f'<div class="marca">{LOGO} EON</div>'
ROD = '<div class="rod"><span>eonsistema.com.br</span><span>@eonsistema</span></div>'


def img(nome):
    return f"file://{E}/img/{nome}"


def feed(corpo, n=None, rod=True):
    return f'<div class="peca f">{MARCA}{f"<div class=num>{n}</div>" if n else ""}{corpo}{ROD if rod else ""}</div>'


def story(corpo):
    return f'<div class="peca s">{MARCA}{corpo}<div class="rod" style="bottom:120px"><span>eonsistema.com.br</span><span>@eonsistema</span></div></div>'


def pagina(corpo):
    return f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{corpo}</body></html>"

