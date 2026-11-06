"""Moldes das peças do Instagram (feed 4:5 e stories 9:16)."""
from estilo import feed, story, img

MASC = img("mascote-eon.png")


def _ck(itens):
    return '<ul class="k">' + "".join(f"<li>{i}</li>" for i in itens) + "</ul>" if itens else ""


def em(t):
    """*destaque* → <em>destaque</em>"""
    p = t.split("*")
    return "".join(f"<em>{x}</em>" if k % 2 else x for k, x in enumerate(p))


def f_titulo(tag, titulo, sub="", check=None, cta=None, masc=False, n=None, tam=96):
    return feed((f'<span class="tag" style="margin-top:56px">{tag}</span>' if tag else '<div style="height:40px"></div>')
                + f'<h1 style="font-size:{tam}px">{em(titulo)}</h1>' + (f'<p class="l">{sub}</p>' if sub else "") + _ck(check)
                + (f'<div class="cta">{cta}</div>' if cta else "")
                + (f'<img class="masc" src="{MASC}" style="width:380px;right:50px;bottom:130px">' if masc else ""), n)


def f_ponto(num, titulo, resp, n):
    return feed(f'<div style="margin-top:90px;font-size:150px;font-weight:800;color:#7be0a6;line-height:1">{num}</div>'
                f'<h2 style="margin-top:20px">{titulo}</h2><div class="caixa" style="margin-top:70px"><span class="tag">No EON</span>'
                f'<p class="l" style="color:#fff;font-size:44px;margin-top:28px">{resp}</p></div>', n)


def f_tela(tag, titulo, sub, tela, n=None):
    return feed(f'<span class="tag" style="margin-top:56px">{tag}</span><h2>{em(titulo)}</h2><p class="l">{sub}</p>'
                f'<div class="tela" style="bottom:118px"><img src="{img(tela)}"></div>', n)


def f_celular(titulo, sub):
    return feed(f'<h1>{em(titulo)}</h1><p class="l" style="max-width:440px">{sub}</p>'
                f'<img src="{img("site/cel_painel.webp")}" style="position:absolute;right:40px;bottom:96px;width:470px">')


def s_texto(tag, titulo, sub="", masc=False, caixa=False, topo=340, lista=None):
    corpo = (f'<span class="tag">{tag}</span>' if tag else "") + f'<h1 style="font-size:{84 if caixa else 92}px">{em(titulo)}</h1>' \
        + (f'<p class="l" style="font-size:44px">{sub}</p>' if sub else "")
    if lista:
        corpo += '<div class="linha" style="margin-top:70px">' + "".join(f"<div><b>{k}</b><span>{v}</span></div>" for k, v in lista) + "</div>"
    corpo = f'<div class="caixa" style="margin-top:{topo}px">{corpo}</div>' if caixa else f'<div style="margin-top:{topo}px">{corpo}</div>'
    if masc:
        corpo += f'<img class="masc" src="{MASC}" style="bottom:260px;width:540px">'
    return story(corpo)


def s_tela(tag, titulo, sub, tela, celular=False):
    if celular:
        t = f'<img src="{img(tela)}" style="position:absolute;left:50%;margin-left:-300px;top:820px;width:600px">'
    else:
        t = (f'<div style="position:absolute;left:40px;right:40px;top:930px;border-radius:28px;overflow:hidden;'
             f'box-shadow:0 30px 80px rgba(0,0,0,.45)"><img src="{img(tela)}" style="width:100%;display:block"></div>')
    return story(f'<div style="margin-top:300px"><span class="tag">{tag}</span><h2>{em(titulo)}</h2><p class="l">{sub}</p></div>' + t)
