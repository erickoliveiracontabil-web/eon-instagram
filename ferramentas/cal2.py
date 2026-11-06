import html, sys
sys.path.insert(0, ".")
from playwright.sync_api import sync_playwright
from estilo import CSS
from plano import DIAS
COR = {"Feed": "#1f5fad", "Reel": "#c2410c", "Story": "#7c3aed"}
cards = ""
for dia, tema, itens in DIAS:
    li = "".join(f'<li class="{"foco" if fo else ""}"><span style="background:{COR[t.split()[0]]}">{t}</span>{html.escape(x)}</li>' for t, x, fo in itens)
    cards += f'<div class="dia"><h3>{dia}<em>{tema}</em></h3><ul>{li}</ul></div>'
tot = sum(len(d[2]) for d in DIAS); fo = sum(x[2] for d in DIAS for x in d[2])
pg = f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}
.cal{{width:1800px;padding:52px;background:#f4f7fb;color:#0f2a4a;font-family:J}}
.cal h1{{font-size:46px;letter-spacing:-1px}} .cal .sub{{font-size:21px;color:#4a5d75;margin:8px 0 30px;display:flex;gap:28px;flex-wrap:wrap}}
.cal .sub i{{display:inline-block;width:14px;height:14px;border-radius:4px;margin-right:7px;vertical-align:-1px}}
.g{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}}
.dia{{background:#fff;border-radius:20px;padding:22px 24px;box-shadow:0 2px 10px rgba(15,42,74,.06)}}
.dia h3{{font-size:25px;margin-bottom:12px}} .dia h3 em{{font-style:normal;color:#0b7f4f;font-size:19px;margin-left:12px}}
.dia ul{{list-style:none}} .dia li{{font-size:18px;font-weight:600;padding:9px 0 9px 0;border-top:1px solid #e8edf4;display:flex;gap:12px;align-items:center;line-height:1.25}}
.dia li span{{flex:none;width:104px;text-align:center;color:#fff;font-size:14px;font-weight:700;padding:4px 0;border-radius:999px}}
.dia li.foco:after{{content:"";flex:none;margin-left:auto;width:14px;height:14px;border-radius:50%;background:#16a34a;box-shadow:0 0 0 4px #dcfce7}}
</style></head><body><div class="cal"><h1>Instagram @eonsistema · sexta, segunda e quarta</h1>
<div class="sub"><span>Por dia: stories 10h, 14h e 18h · feed 11h · reel 17h com o mascote (12 s)</span>
<span><i style="background:#16a34a"></i>Foco "nota sem trava": {fo} de {tot} publicações ({fo*100//tot}%)</span></div>
<div class="g">{cards}</div></div></body></html>"""
open("out/_cal.html", "w").write(pg)
with sync_playwright() as p:
    b = p.chromium.launch(); pa = b.new_page(viewport={"width": 1900, "height": 1200})
    pa.goto("file://" + __import__("os").path.abspath("out/_cal.html")); pa.wait_for_timeout(300)
    pa.locator(".cal").screenshot(path="out/calendario.png"); b.close()
