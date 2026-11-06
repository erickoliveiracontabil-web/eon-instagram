"""Reel do mascote EON conversando com quem assiste, com locução (voz MBROLA br3 via espeak-ng, um pouco mais aguda).
O balão digita no ritmo da fala e o mascote se mexe pelo volume da voz, suavizado (sem tremer).
Uso: from reel import gerar; gerar(["Oi! Eu sou o *EON*.", ...], "saida.mp4")"""
import json
import math
import os
import re
import subprocess
import tempfile
import wave

import numpy as np
from playwright.sync_api import sync_playwright

from estilo import CSS, E, LOGO

FPS = 30
SR = 44100
PAUSA = 0.22      # respiro entre falas
FINAL = 1.6       # tempo do botão final
VOZ = ["-v", "mb-br3", "-s", "158", "-p", "58"]
TOM = 1.12        # sobe o tom sem mudar a velocidade

FONETICA = [(r"NFS-e", "ene éfe ésse é"), (r"NFC-e", "ene éfe cê é"), (r"NF-e", "ene éfe é"), (r"\bEON\b", "Éon"),
            (r"\bA1\b", "á um"), (r"\bXML\b", "xis éme éle"), (r"\bDANFE\b", "dânfi"), (r"\bPix\b", "píx"),
            (r"\bSefaz\b", "Sefáz"), (r"\b48\b", "quarenta e oito"), (r"\b30\b", "trinta"), (r"\bWhatsApp\b", "uótsáp"), (r"R\$ 139,90", "cento e trinta e nove reais e noventa centavos"), (r"\bIBS\b", "í bê ésse"), (r"\bCBS\b", "cê bê ésse"), (r"\bXMLs\b", "xis éme éles")]

PAGINA = """<!doctype html><html><head><meta charset=utf-8><style>%s
body{margin:0;background:#0b1f38}
#r{position:relative;width:1080px;height:1920px;overflow:hidden;color:#fff;font-family:J;
   background:radial-gradient(110%% 70%% at 50%% 78%%,#235792 0%%,#0f2a4a 55%%,#0a1b31 100%%)}
#r .marca{position:absolute;left:88px;top:150px}
#bal{position:absolute;left:90px;right:90px;top:430px;background:#fff;color:#0f2a4a;border-radius:48px;padding:56px 60px;
     font-size:70px;line-height:1.16;font-weight:800;letter-spacing:-1px;box-shadow:0 30px 70px rgba(0,0,0,.35);transform-origin:50%% 100%%}
#bal:after{content:"";position:absolute;left:50%%;bottom:-38px;margin-left:-40px;border:40px solid transparent;border-top-color:#fff;border-bottom:0}
#bal em{font-style:normal;color:#0b7f4f}
#cur{display:inline-block;width:8px;height:66px;background:#0b7f4f;margin-left:6px;vertical-align:-8px}
#m{position:absolute;left:50%%;bottom:250px;width:640px;margin-left:-320px;transform-origin:50%% 100%%}
#sombra{position:absolute;left:50%%;bottom:225px;width:420px;height:60px;margin-left:-210px;border-radius:50%%;background:rgba(0,0,0,.35);filter:blur(14px)}
#cta{position:absolute;left:0;right:0;top:0;text-align:center;opacity:0}
#cta span{display:inline-block;background:#0b7f4f;color:#fff;font-weight:800;font-size:54px;padding:30px 54px;border-radius:26px;box-shadow:0 18px 40px rgba(0,0,0,.35)}
#ondas{position:absolute;left:50%%;bottom:760px;margin-left:255px;display:flex;align-items:center;gap:10px;height:90px}
#ondas i{display:block;width:14px;border-radius:7px;background:#7be0a6}
</style></head><body><div id=r><div class=marca>%s EON</div><div id=sombra></div>
<img id=m src="file://%s/img/mascote-eon.png"><div id=ondas><i></i><i></i><i></i></div>
<div id=bal><span id=tx></span><span id=cur></span></div><div id=cta><span></span></div></div>
<script>
const F=%s, ENV=%s, FPS=%d;
const suave=x=>x<0?0:x>1?1:x*x*(3-2*x);
function quadro(t){
  let i=0; while(i<F.length-1 && t>=F[i+1].ini) i++;
  const f=F[i], dt=t-f.ini, fr=Math.max(0,Math.min(1,(t-f.fala)/f.dur));
  const n=Math.round(f.txt.length*fr);
  let r=n,h='';for(const g of f.seg){const k=Math.min(r,g[0].length);r-=k;const x=g[0].slice(0,k).replace(/&/g,'&amp;').replace(/</g,'&lt;');h+=g[1]?'<em>'+x+'</em>':x;}
  document.getElementById('tx').innerHTML=h;
  document.getElementById('cur').style.opacity=(n<f.txt.length||Math.floor(t*2)%%2==0)?1:0;
  const b=document.getElementById('bal'), pop=suave(dt/.25);
  b.style.transform=`scale(${.92+.08*pop})`; b.style.opacity=suave(dt/.15);
  const e=ENV[Math.min(ENV.length-1,Math.round(t*FPS))]||0;
  // inclina para um lado a cada fala, devagar; respira; sobe um pouco quando a voz sobe
  let ang=0; for(let k=0;k<=i;k++){const w=suave((t-F[k].ini)/.6); ang=ang*(1-w)+(k%%2?-2.2:2.2)*w;}
  const resp=Math.sin(t*Math.PI)*6, ent=suave(t/.6);
  const y=(1-ent)*520 + resp - e*16;
  document.getElementById('m').style.transform=`translateY(${y}px) rotate(${ang}deg) scale(${1+e*.012},${1+e*.02})`;
  document.getElementById('sombra').style.transform=`scaleX(${1-(resp-e*16)/220})`;
  const o=document.getElementById('ondas'); o.style.opacity=Math.min(1,e*3);
  [...o.children].forEach((x,k)=>{x.style.height=(16+64*e*(.7+.3*Math.sin(t*5+k*1.7)))+'px'});
  const c=document.getElementById('cta');
  if(f.cta){const a=suave((t-f.fala-f.dur-.1)/.35); c.style.opacity=a;
    c.style.top=(b.offsetTop+b.offsetHeight+80)+'px'; c.firstChild.textContent=f.cta; c.style.transform=`translateY(${(1-a)*30}px)`}
  else c.style.opacity=0;
}
</script></body></html>"""


def _fala(texto):
    """'Sua nota sai *sem trava*' → texto puro e trechos [(texto, destacado)]."""
    seg = [[p, k % 2 == 1] for k, p in enumerate(texto.split("*")) if p]
    return "".join(p for p, _ in seg), seg


def falado(txt):
    for a, b in FONETICA:
        txt = re.sub(a, b, txt)
    return txt


def _voz(txt, pasta, k):
    """Gera a fala em WAV 44,1 kHz mono, tom ajustado e volume normalizado; devolve as amostras float."""
    bruto, final = f"{pasta}/v{k}.wav", f"{pasta}/v{k}f.wav"
    subprocess.run(["espeak-ng", *VOZ, "-w", bruto, falado(txt)], check=True)
    with wave.open(bruto) as w:
        taxa = w.getframerate()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", bruto, "-af",
                    f"asetrate={taxa}*{TOM},aresample={SR},atempo={1 / TOM:.4f},highpass=f=90,"
                    "acompressor=threshold=-18dB:ratio=3:attack=5:release=80,loudnorm=I=-15:TP=-1.5",
                    "-ac", "1", "-ar", str(SR), final], check=True)
    with wave.open(final) as w:
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    nz = np.nonzero(np.abs(a) > 0.01)[0]  # corta silêncio das pontas
    return a[max(0, nz[0] - 400): nz[-1] + 1200] if len(nz) else a


def _carregar(caminho, pasta, acel=1.0):
    """Áudio externo (voz humanizada) → mono 44,1 kHz com volume normalizado."""
    destino = f"{pasta}/externo.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", caminho, "-af", f"atempo={acel},highpass=f=70,loudnorm=I=-15:TP=-1.5",
                    "-ac", "1", "-ar", str(SR), destino], check=True)
    with wave.open(destino) as w:
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768


def _dividir(a, textos):
    """Divide a locução em um trecho por fala. Testa todas as combinações de pausas como fronteira e fica com a
    que deixa a duração falada de cada trecho mais proporcional ao número de letras da fala. Pausas longas dentro
    do trecho são encurtadas para deixar a fala mais dinâmica."""
    from itertools import combinations
    n, q = len(textos), int(SR * 0.02)
    rms = np.array([np.sqrt(np.mean(a[i:i + q] ** 2)) for i in range(0, len(a), q)])
    mudo = rms < max(0.012, rms.max() * 0.04)
    voz = np.nonzero(~mudo)[0]
    ini, fim = voz[0], voz[-1]
    def _pausas(minimo):
        r, i = [], ini
        while i < fim:
            if mudo[i]:
                j = i
                while j < fim and mudo[j]:
                    j += 1
                if j - i >= minimo:
                    r.append((i, j))
                i = j
            else:
                i += 1
        return r
    for minimo in (6, 4, 2, 1):
        pausas = _pausas(minimo)
        if len(pausas) >= n - 1:
            break
    falado = np.cumsum(~mudo)
    letras = np.array([len(t) for t in textos], float)
    total = falado[fim] - falado[ini]
    esperado = letras / letras.sum() * total
    melhor, custo_min = [], None
    for comb in combinations(pausas, n - 1):
        lim = [ini] + [(x[0] + x[1]) // 2 for x in comb] + [fim]
        real = np.array([falado[lim[k + 1]] - falado[lim[k]] for k in range(n)], float)
        custo = float(np.sum(np.abs(real - esperado) / esperado))
        if custo_min is None or custo < custo_min:
            melhor, custo_min = comb, custo
    lim = [0] + [((x[0] + x[1]) // 2) * q for x in melhor] + [len(a)]
    global LIMITES
    LIMITES = [round(x / SR, 2) for x in lim[1:-1]]
    partes = []
    for k in range(len(lim) - 1):
        p = a[lim[k]:lim[k + 1]]
        nz = np.nonzero(np.abs(p) > 0.01)[0]
        p = p[max(0, nz[0] - 600): nz[-1] + 1500] if len(nz) else p
        partes.append(_encurtar(p))
    return partes


def _encurtar(p, maximo=0.16):
    """Encurta silêncios internos maiores que `maximo` segundos."""
    q = int(SR * 0.02)
    rms = np.array([np.sqrt(np.mean(p[i:i + q] ** 2)) for i in range(0, len(p), q)])
    mudo = rms < max(0.012, rms.max() * 0.04)
    sai, i, lim = [], 0, int(maximo / 0.02)
    while i < len(mudo):
        j = i
        while j < len(mudo) and mudo[j] == mudo[i]:
            j += 1
        bloco = p[i * q:j * q]
        if mudo[i] and j - i > lim:
            m = lim * q // 2
            bloco = np.concatenate([bloco[:m], bloco[-m:]])
        sai.append(bloco)
        i = j
    return np.concatenate(sai)


def gerar(falas, saida, cta="Teste grátis · link na bio", voz=None, faladas=None, acel=1.0):
    """falas: lista de textos (use *assim* para destacar em verde). A última recebe o botão de chamada."""
    saida = os.path.abspath(saida)
    pasta = tempfile.mkdtemp(prefix="reel")
    F, trilha, t = [], [np.zeros(int(SR * 0.6), np.float32)], 0.6
    partes = _dividir(_carregar(voz, pasta, acel), faladas or [_fala(f)[0] for f in falas]) if voz else None
    for k, fz in enumerate(falas):
        txt, seg = _fala(fz)
        a = partes[k] if partes else _voz(txt, pasta, k)
        dur = len(a) / SR
        F.append({"ini": t - 0.25 if k else 0, "fala": t, "dur": dur, "txt": txt, "seg": seg,
                  "cta": cta if k == len(falas) - 1 else ""})
        trilha += [a, np.zeros(int(SR * (FINAL if k == len(falas) - 1 else PAUSA)), np.float32)]
        t += dur + (FINAL if k == len(falas) - 1 else PAUSA)
    audio = np.concatenate(trilha)
    total = len(audio) / SR
    with wave.open(f"{pasta}/trilha.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(audio, -1, 1) * 32767).astype(np.int16).tobytes())
    # envelope por quadro, suavizado (sobe rápido, desce devagar) e sem picos: é o que tira o tremor
    passo = SR // FPS
    rms = np.array([np.sqrt(np.mean(audio[i:i + passo] ** 2)) for i in range(0, len(audio), passo)])
    rms = np.clip(rms / (np.percentile(rms[rms > 0], 95) if (rms > 0).any() else 1), 0, 1)
    env, v = [], 0.0
    for x in rms:
        v += (x - v) * (0.35 if x > v else 0.12)
        env.append(round(float(v), 3))
    pag = PAGINA % (CSS, LOGO, E, json.dumps(F, ensure_ascii=False), json.dumps(env), FPS)
    tmp = f"{pasta}/reel.html"
    open(tmp, "w").write(pag)
    temp_mp4 = saida[:-4] + ".parcial.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                           "-i", f"{pasta}/trilha.wav", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
                           "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "128k", "-ar", str(SR), "-ac", "2",
                           "-shortest", "-movflags", "+faststart", temp_mp4], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto("file://" + tmp)
        pg.wait_for_timeout(400)
        for i in range(math.ceil(total * FPS)):
            pg.evaluate(f"quadro({i / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
        br.close()
    ff.stdin.close()
    if ff.wait() == 0:
        os.replace(temp_mp4, saida)
    return total
