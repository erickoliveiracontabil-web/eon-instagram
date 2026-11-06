"""Produz os dias 11/11 a 02/12 (e refaz o reel de 09/11 com voz). Uso: python3 produzir.py <pasta_saida> [AAAA-MM-DD ...]"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modelos import f_celular, f_ponto, f_tela, f_titulo, s_tela, s_texto
from pecas import render
from reel import gerar

HT = "\n\n#notafiscal #nfe #nfse #emissordenotas #eonsistema"
CTA_LEG = "\n\nTeste grátis por 48 horas: link na bio."

DIAS = {
    "2026-11-09": {"reel": ["Segunda-feira e o portal *fora do ar*?", "Respira. Comigo a nota sai *por dentro do sistema*.",
                            "Cliente e produto já cadastrados: é só *conferir e emitir*.", "Bora começar a semana *sem trava*?"]},
    "2026-11-11": {
        "s10": (s_texto("Bom dia", "Nota emitida cedo, *dia tranquilo.*", "Quarta-feira começou. Bora tirar as notas da frente?"), False),
        "feed": [f_titulo("NFS-e sem trava", "NFS-e em 1 minuto, *sem portal da prefeitura.*",
                          "Tomador cadastrado, serviço escolhido, nota emitida.",
                          ["Envio por e-mail ao tomador", "XML e PDF guardados no sistema", "Funciona no celular"])],
        "leg": "NFS-e em 1 minuto, sem portal da prefeitura. ⏱️\n\nQuem presta serviço conhece a novela: site lento, sessão que cai, campo que some. No EON é tomador, serviço, valor e pronto: a nota sai de dentro do sistema e fica guardada com XML e PDF." + CTA_LEG + "\n\n#nfse #prestadordeservico #mei #autonomo #notafiscal #eonsistema",
        "s14": (s_texto("Passo a passo", "Sua NFS-e no EON", "", caixa=True, topo=300,
                        lista=[("1", "Escolha o tomador"), ("2", "Escolha o serviço"), ("3", "Confira o valor"), ("4", "Toque em emitir")]), False),
        "s18": (s_texto("Caixinha", "Qual sua maior dúvida com *nota fiscal?*", "Manda aqui que a gente responde nos stories."), True),
        "reel": ["Presta serviço e sofre pra emitir *NFS-e*?", "O portal da prefeitura *travou de novo*?",
                 "Comigo é tomador, serviço, valor e *pronto*.", "A nota sai *sem trava*. Bora testar?"],
        "legr": "Presta serviço e sofre com o portal da prefeitura? 😩\n\nNo EON a NFS-e sai em poucos cliques: tomador, serviço, valor e pronto." + CTA_LEG + "\n\n#nfse #prestadordeservico #notafiscal #eonsistema",
    },
    "2026-11-13": {
        "s10": (s_texto("Sextou", "As notas da semana *estão em dia?*", "Sexta é dia de fechar tudo e descansar tranquilo."), False),
        "feed": "reforma",
        "leg": "Reforma tributária: o que muda na sua nota? 📅\n\nEm 2026 o IBS e a CBS já aparecem nas notas em fase de teste. Em 2027 a CBS começa a ser cobrada e PIS e Cofins deixam de existir. De 2029 a 2032 ICMS e ISS diminuem até virar IBS.\n\nNo EON você não precisa acompanhar cada norma: o sistema é atualizado e a nota sai no leiaute certo.\n\nSalve este post para consultar depois. 📌" + CTA_LEG + "\n\n#reformatributaria #ibs #cbs #notafiscal #contabilidade #eonsistema",
        "s14": (s_texto("Reforma tributária", "A nota mudou. *O EON já se atualizou.*", "IBS e CBS já saem nas suas notas, no leiaute novo, sem você mexer em nada.", caixa=True), False),
        "s18": (s_texto("", "Salve o carrossel *da reforma* 📌", "Está no nosso feed. Vale ter à mão em 2027.", masc=True), False),
        "reel": ["Reforma tributária te deixou *confuso*?", "IBS, CBS, leiaute novo... *deixa comigo*.",
                 "Eu me atualizo e sua nota sai *no padrão certo*.", "Você só emite. *Bora testar?*"],
        "legr": "Reforma tributária te deixou confuso? 🤯\n\nIBS, CBS, leiaute novo... o EON se atualiza a cada norma e sua nota sai no padrão certo. Você só emite." + CTA_LEG + "\n\n#reformatributaria #ibs #cbs #eonsistema",
    },
    "2026-11-16": {
        "s10": (s_texto("Enquete", "Você já emitiu nota *pelo celular?*"), True),
        "feed": [f_celular("Suas notas *no bolso.*", "Emita NF-e e NFS-e pelo celular, sem instalar nada.")],
        "leg": "Suas notas no bolso. 📱\n\nCliente pediu a nota e você está na rua? No EON a NF-e e a NFS-e saem pelo celular, direto do navegador. Sem app para instalar, sem portal travando." + CTA_LEG + HT,
        "s14": (s_tela("No celular", "Assim fica o EON *na palma da mão.*", "Início, vendas e notas a um toque.", "site/cel_painel.webp", celular=True), False),
        "s18": (s_texto("Suporte", "Suporte por WhatsApp *de gente de verdade.*", "Travou em alguma coisa? Chama a gente.", caixa=True), False),
        "reel": ["Tá na rua e o cliente pediu a *nota*?", "Abre o celular e *me chama*.",
                 "A *NF-e* sai do celular mesmo, sem instalar nada.", "Simples assim. *Bora testar?*"],
        "legr": "Tá na rua e o cliente pediu a nota? 📲\n\nAbre o celular: no EON a NF-e sai pelo navegador, sem instalar nada." + CTA_LEG + HT,
    },
    "2026-11-18": {
        "s10": (s_texto("Pergunta rápida", "Você sabe quando vence seu *certificado A1?*"), False),
        "feed": [f_titulo("Certificado digital", "Certificado vencido *trava a nota.*",
                          "O EON avisa no Início quando o seu A1 está perto de vencer.",
                          ["Aviso antes do vencimento", "Sem susto na hora de emitir", "Renovou? É só enviar o arquivo novo"])],
        "leg": "Certificado vencido trava a nota. 🔒\n\nE ninguém lembra da data até o dia em que a nota não sai. No EON o aviso aparece no Início quando o seu A1 está perto de vencer, com tempo de renovar sem correria." + CTA_LEG + HT,
        "s14": (s_texto("Dica", "No EON o aviso aparece *logo no Início.*", "Abriu o sistema, viu o prazo do certificado.", caixa=True), False),
        "s18": (s_texto("Nota sem trava", "Nota rejeitada? *O EON explica em português.*", "Nada de código misterioso: você vê o que ajustar e emite de novo.", caixa=True), False),
        "reel": ["Seu certificado digital vence *quando*?", "Se ele vence, a nota *trava*.",
                 "Mas fica tranquilo: eu te *aviso antes*.", "Nota sem susto. *Bora testar?*"],
        "legr": "Seu certificado digital vence quando? 📅\n\nSe ele vence, a nota trava. No EON o aviso vem antes." + CTA_LEG + HT,
    },
    "2026-11-20": {
        "s10": (s_texto("Sexta-feira", "Dia de *faturamento?*", "Bora que as notas saem rapidinho."), False),
        "feed": [f_titulo("NF-e sem trava", "NF-e do cadastro *até o cliente.*", "Arraste para o lado →", n="1/5", tam=104),
                 f_ponto(1, "Cliente e produtos já cadastrados", "Você escolhe na lista. Nada de digitar CNPJ e NCM toda vez.", "2/5"),
                 f_ponto(2, "Conferência antes de enviar", "O EON confere os dados e manda para a Sefaz de dentro do sistema.", "3/5"),
                 f_ponto(3, "Autorizou, está pronto", "DANFE e XML na hora para enviar ao cliente, e o estoque já baixa.", "4/5"),
                 f_titulo("", "Nota fiscal *sem trava.*", "", ["NF-e e NFS-e em poucos cliques", "Computador ou celular", "Teste grátis por 48 horas"], cta="Link na bio →", masc=True, n="5/5")],
        "leg": "NF-e do cadastro até o cliente, sem passar pelo portal. 🧾\n\n1. Cliente e produtos já cadastrados\n2. O EON confere e envia para a Sefaz\n3. Autorizou: DANFE e XML na hora, e o estoque já baixa\n\nSalve para mostrar para quem ainda emite no site. 📌" + CTA_LEG + HT,
        "s14": (s_tela("Nota autorizada", "DANFE e XML *na hora.*", "Pronto para mandar ao cliente.", "site/nfe.webp"), False),
        "s18": (s_texto("", "Bom fim de semana! *Segunda tem mais.*", "", masc=True), False),
        "reel": ["Nota de venda pra empresa? *NF-e* comigo.", "Cliente e produto já cadastrados, eu *confiro tudo*.",
                 "Autorizou? DANFE e XML *na hora*.", "E o estoque já baixa. *Bora testar?*"],
        "legr": "Nota de venda para empresa? NF-e com o EON. ✅\n\nCadastro pronto, conferência antes do envio, DANFE e XML na hora e estoque atualizado." + CTA_LEG + HT,
    },
    "2026-11-23": {
        "s10": (s_texto("Enquete", "Sua loja vai participar da *Black Friday?*"), True),
        "feed": [f_titulo("Black Friday", "Seu caixa aguenta a *Black Friday?*", "Fila grande pede nota rápida, estoque certo e caixa fechando no fim do dia.",
                          ["NFC-e em segundos", "Estoque baixando a cada venda", "Fechamento de caixa simples"])],
        "leg": "Seu caixa aguenta a Black Friday? 🛍️\n\nFila grande pede NFC-e rápida, estoque certo e caixa fechando sem drama. No EON está tudo no mesmo lugar." + CTA_LEG + "\n\n#blackfriday #varejo #nfce #frentedecaixa #eonsistema",
        "s14": (s_tela("Nota sem trava", "NFC-e em segundos, *sem segurar a fila.*", "Produto, pagamento, nota autorizada.", "site/caixa.webp"), False),
        "s18": (s_texto("Checklist da semana", "Antes da sexta:", "", caixa=True, topo=300,
                        lista=[("✓", "Certificado digital em dia"), ("✓", "Preços conferidos"), ("✓", "Estoque contado"), ("✓", "Troco no caixa")]), False),
        "reel": ["Black Friday chegando e o caixa *lotado*?", "Comigo a *NFC-e* sai em segundos.",
                 "Cliente feliz, fila andando, *nota emitida*.", "Prepara o caixa. *Bora testar?*"],
        "legr": "Black Friday chegando e o caixa lotado? 🛒\n\nNo EON a NFC-e sai em segundos e a fila anda." + CTA_LEG + "\n\n#blackfriday #nfce #varejo #eonsistema",
    },
    "2026-11-25": {
        "s10": (s_texto("Bom dia", "Estoque conferido *para sexta?*"), False),
        "feed": [f_titulo("Estoque", "Estoque acabando *vira aviso.*", "O EON mostra no Início os produtos abaixo do mínimo.",
                          ["Aviso antes de faltar", "Baixa automática a cada nota", "Lista pronta para repor"])],
        "leg": "Estoque acabando vira aviso. 📦\n\nNada de descobrir na hora da venda que o produto acabou. No EON o Início mostra o que está abaixo do mínimo, e cada nota emitida já baixa o estoque." + CTA_LEG + "\n\n#estoque #gestao #varejo #eonsistema",
        "s14": (s_texto("Nota sem trava", "Vendeu com nota, *o estoque baixa sozinho.*", "Sem planilha, sem conta de cabeça.", caixa=True), False),
        "s18": (s_texto("Você sabia?", "Se a Sefaz cair, *a NFC-e sai em contingência.*", "A venda não para e a nota é transmitida depois, dentro do prazo.", caixa=True), False),
        "reel": ["Acabou o produto *bem na hora* da venda?", "Comigo o estoque *avisa antes*.",
                 "E cada nota emitida já *baixa o estoque*.", "Tudo no mesmo lugar. *Bora testar?*"],
        "legr": "Acabou o produto bem na hora da venda? 😬\n\nNo EON o estoque avisa antes e cada nota já dá baixa." + CTA_LEG + "\n\n#estoque #nfce #eonsistema",
    },
    "2026-11-27": {
        "s10": (s_texto("Black Friday", "Boas vendas *hoje!* 🛍️", "", masc=True), False),
        "feed": [f_titulo("Nota sem trava", "Black Friday com nota em dia, *sem travar o caixa.*",
                          "Movimento alto não combina com portal fora do ar. No EON a nota sai de dentro do sistema.", tam=88)],
        "leg": "Black Friday com nota em dia e o caixa andando. 🧾\n\nMovimento alto não combina com portal fora do ar. No EON a nota sai de dentro do sistema e, se a Sefaz cair, a NFC-e segue em contingência." + CTA_LEG + "\n\n#blackfriday #nfce #notafiscal #eonsistema",
        "s14": (s_texto("Nota sem trava", "Movimento alto? *A nota não para.*", "", caixa=True), False),
        "s18": (s_texto("Caixinha", "Como foram as vendas *hoje?*", "Conta pra gente aqui."), True),
        "reel": ["Hoje é *Black Friday*!", "Pode vender à vontade que a *nota é comigo*.",
                 "Sem portal travando, *sem fila parada*.", "Boas vendas! *Bora testar?*"],
        "legr": "Hoje é Black Friday! 🛍️ Pode vender à vontade que a nota é com o EON." + CTA_LEG + "\n\n#blackfriday #nfce #eonsistema",
    },
    "2026-11-30": {
        "s10": (s_texto("Enquete", "Contador: você ainda emite nota *pelos seus clientes?*"), True),
        "feed": [f_titulo("Para o contador", "Contador, *tudo num painel só.*", "Arraste para o lado →", n="1/5", tam=104),
                 f_tela("Painel do contador", "Todos os clientes *numa tela.*", "Notas, pendências e documentos.", "site/contador.webp", n="2/5"),
                 f_ponto(1, "XML de todos num arquivo só", "Baixe os XMLs do mês dos clientes de uma vez.", "3/5"),
                 f_ponto(2, "O cliente emite a própria nota", "Sem portal e sem pedir para você: a nota sai de dentro do EON.", "4/5"),
                 f_titulo("", "Menos portal, *menos retrabalho.*", "", ["Indique o EON aos seus clientes", "Teste grátis por 48 horas"], cta="Link na bio →", n="5/5")],
        "leg": "Contador, tudo num painel só. 📊\n\nClientes, notas e documentos numa tela, XMLs do mês num arquivo só, e o cliente emitindo a própria nota sem portal." + CTA_LEG + "\n\n#contabilidade #contador #escritoriocontabil #xml #eonsistema",
        "s14": (s_tela("Para o contador", "XML de todos os clientes *num lugar só.*", "Baixou, mandou para a escrita fiscal.", "site/contador.webp"), False),
        "s18": (s_texto("", "Indique o EON *aos seus clientes.*", "Nota sem trava para eles, menos retrabalho para você.", masc=True), False),
        "reel": ["Contador, chega de *um portal por cliente*.", "Comigo seus clientes emitem a nota *sozinhos*.",
                 "E você pega todos os *XMLs num clique*.", "Menos retrabalho. *Bora testar?*"],
        "legr": "Contador, chega de um portal por cliente. 🙌\n\nNo EON seus clientes emitem a própria nota e você baixa todos os XMLs num clique." + CTA_LEG + "\n\n#contador #contabilidade #eonsistema",
    },
    "2026-12-02": {
        "s10": (s_texto("Nota sem trava", "Quanto custa emitir sem trava? *R$ 4,66 por dia.*", "No plano EON de R$ 139,90 por mês.", caixa=True), False),
        "feed": [f_titulo("Plano EON", "A partir de *R$ 139,90 por mês.*", "Nota fiscal sem trava e gestão no mesmo lugar.",
                          ["Teste grátis por 48 horas", "Pix ou cartão em até 12x", "Suporte por WhatsApp"], cta="Link na bio →")],
        "leg": "Quanto custa emitir nota sem trava? 💡\n\nO plano EON começa em R$ 139,90 por mês, menos de R$ 5 por dia. Teste grátis por 48 horas na sua empresa de verdade, e contrate com Pix ou cartão em até 12x." + CTA_LEG + HT,
        "s14": (s_texto("Pagamento", "Pix ou cartão *em até 12x.*", "O plano é liberado assim que o pagamento é confirmado.", caixa=True), False),
        "s18": (s_texto("Ficou dúvida?", "Perguntas frequentes *no site.*", "eonsistema.com.br"), False),
        "reel": ["Quer emitir nota *sem trava*?", "Me testa por *48 horas*, de graça.",
                 "Na sua empresa de verdade, *sem instalar nada*.", "Depois, a partir de R$ 139,90 por mês. *Bora?*"],
        "legr": "Quer emitir nota sem trava? Testa o EON por 48 horas, de graça. 🚀" + CTA_LEG + HT,
    },
}

if __name__ == "__main__":
    base = os.path.abspath(sys.argv[1])
    so = sys.argv[2:]
    REF = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "artes")
    for dia, d in DIAS.items():
        if so and dia not in so:
            continue
        pasta = f"{base}/{dia}"
        os.makedirs(pasta, exist_ok=True)
        pecas = {}
        if isinstance(d.get("feed"), list):
            for k, h in enumerate(d["feed"], 1):
                pecas[f"feed{k}"] = h
        for h in ("s10", "s14", "s18"):
            if h in d:
                pecas[f"story{h[1:]}"] = d[h][0]
        if pecas:
            render(pecas, pasta)
        if d.get("feed") == "reforma":
            from PIL import Image
            for k in (1, 2, 3):
                Image.open(f"{REF}/04_reforma_{k}.png").convert("RGB").save(f"{pasta}/feed{k}.jpg", quality=92)
        if os.path.exists(f"{pasta}/_t.html"):
            os.remove(f"{pasta}/_t.html")
        if not os.path.exists(f"{pasta}/reel_voz.mp4"):
            print(dia, gerar(d["reel"], f"{pasta}/reel_voz.mp4"), flush=True)
