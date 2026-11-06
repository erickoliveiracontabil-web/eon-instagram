"""Monta o reel de um dia com a locução pronta em locucao/<dia>.mp3 (voz Caio, Speko/Azure).
Uso: python3 ferramentas/montar_reels.py 2026-11-09  → gera <dia>/reel_alegre.mp4"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from produzir import DIAS
from reel import gerar, _fala
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FALAS = {d: v["reel"] for d, v in DIAS.items()}
FALAS["2026-11-06"] = ["Oi! Eu sou o *EON*.", "O portal do governo travou *de novo* na hora da nota?",
                       "Comigo, sua *NF-e* e sua *NFS-e* saem em poucos cliques.", "Sem trava e sem fila. *Bora testar?*"]
SUB = [(r"NFS-e", "ene-éfe-ésse-é"), (r"NFC-e", "ene-éfe-cê-é"), (r"NF-e", "ene-éfe-é"), (r"XMLs", "xis-eme-eles"),
       (r"XML", "xis-eme-ele"), (r"\b48\b", "quarenta e oito"), (r"R\$ 139,90", "cento e trinta e nove e noventa")]
def falado(t):
    t = _fala(t)[0]
    for a, b in SUB:
        t = re.sub(a, b, t)
    return t
dia = sys.argv[1]
f = FALAS[dia]
ACEL = 1.08 if dia == "2026-11-06" else 1.22
print(dia, gerar(f, f"{REPO}/{dia}/reel_alegre.mp4", voz=f"{REPO}/locucao/{dia}.mp3", faladas=[falado(x) for x in f], acel=ACEL), flush=True)
