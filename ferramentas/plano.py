"""Plano das 4 primeiras semanas (sexta, segunda e quarta). F = foco "nota sem trava" (NF-e/NFS-e sem depender do portal).
Cada dia: feed 11h, stories 10h/14h/18h e reel 17h."""

DIAS = [
    ("Sex 06/11", "Apresentação", [
        ("Story 10h", "Hora de fechar a semana: as notas já saíram?", 0), ("Feed 11h", "A nota não pode esperar o portal voltar", 1),
        ("Story 14h", "Você sabia? Sem entrar no portal do governo", 1), ("Reel 17h", "EON: \"Portal travou de novo?\"", 1),
        ("Story 18h", "O EON tem um recado pra você", 0)]),
    ("Seg 09/11", "Segunda sem fila", [
        ("Story 10h", "Enquete: já perdeu tempo com portal travado?", 1), ("Feed 11h", "Carrossel: 3 travas do portal que somem no EON", 1),
        ("Story 14h", "Bastidor: a NF-e saindo na tela do EON", 1), ("Reel 17h", "EON: \"Segunda e o portal fora do ar? Comigo não\"", 1),
        ("Story 18h", "Clientes e produtos: cadastra uma vez só", 0)]),
    ("Qua 11/11", "Prestador de serviço", [
        ("Story 10h", "Bom dia! Nota emitida cedo é dia tranquilo", 0), ("Feed 11h", "NFS-e em 1 minuto, sem portal da prefeitura", 1),
        ("Story 14h", "Passo a passo da NFS-e no EON", 1), ("Reel 17h", "EON: \"Presta serviço? A NFS-e sai comigo\"", 1),
        ("Story 18h", "Caixinha: qual sua maior dúvida com nota?", 0)]),
    ("Sex 13/11", "Reforma tributária", [
        ("Story 10h", "Sextou! Notas da semana em dia?", 0), ("Feed 11h", "Carrossel: o que muda na sua nota em 2027", 0),
        ("Story 14h", "A nota mudou e o EON já se atualizou", 1), ("Reel 17h", "EON: \"Reforma? Deixa que eu me atualizo\"", 0),
        ("Story 18h", "Salve o carrossel da reforma", 0)]),
    ("Seg 16/11", "Nota do celular", [
        ("Story 10h", "Enquete: você emite nota pelo celular?", 1), ("Feed 11h", "Seu caixa e suas notas no bolso", 1),
        ("Story 14h", "Print: NF-e emitida pelo celular", 1), ("Reel 17h", "EON: \"Tá na rua? A nota sai do celular\"", 1),
        ("Story 18h", "Suporte por WhatsApp de gente de verdade", 0)]),
    ("Qua 18/11", "Certificado digital", [
        ("Story 10h", "Quando vence seu certificado A1?", 0), ("Feed 11h", "Certificado vencido trava a nota. O EON avisa antes", 1),
        ("Story 14h", "Onde o EON mostra o vencimento", 0), ("Reel 17h", "EON: \"Seu certificado vence quando? Eu te aviso\"", 0),
        ("Story 18h", "Nota rejeitada? O EON explica o motivo em português", 1)]),
    ("Sex 20/11", "NF-e para empresas", [
        ("Story 10h", "Sexta de faturamento?", 0), ("Feed 11h", "Carrossel: NF-e do pedido ao e-mail do cliente", 1),
        ("Story 14h", "DANFE e XML direto no WhatsApp do cliente", 1), ("Reel 17h", "EON: \"Nota emitida já vai pro cliente\"", 1),
        ("Story 18h", "Bom fim de semana!", 0)]),
    ("Seg 23/11", "Semana da Black Friday", [
        ("Story 10h", "Enquete: sua loja participa da Black Friday?", 0), ("Feed 11h", "Seu caixa aguenta a Black Friday?", 0),
        ("Story 14h", "NFC-e em segundos, sem segurar a fila", 1), ("Reel 17h", "EON: \"Fila no caixa? A nota sai rapidinho\"", 1),
        ("Story 18h", "Checklist do caixa para a semana", 0)]),
    ("Qua 25/11", "Estoque e vendas", [
        ("Story 10h", "Estoque conferido para sexta?", 0), ("Feed 11h", "Estoque acabando vira aviso no EON", 0),
        ("Story 14h", "Vendeu com nota, o estoque baixa sozinho", 1), ("Reel 17h", "EON: \"Seu estoque fala comigo\"", 0),
        ("Story 18h", "Se a Sefaz cair, a NFC-e sai em contingência", 1)]),
    ("Sex 27/11", "Black Friday", [
        ("Story 10h", "Boas vendas hoje!", 0), ("Feed 11h", "Black Friday com nota em dia, sem travar o caixa", 1),
        ("Story 14h", "Movimento alto? A nota não para", 1), ("Reel 17h", "EON: \"Hoje é dia de vender, a nota é comigo\"", 1),
        ("Story 18h", "Como foram as vendas? Conta pra gente", 0)]),
    ("Seg 30/11", "Para o contador", [
        ("Story 10h", "Contador, quantas notas você emite pelo cliente?", 1), ("Feed 11h", "Carrossel: o contador acompanha tudo num painel", 0),
        ("Story 14h", "XML de todos os clientes num lugar só", 0), ("Reel 17h", "EON: \"Contador, chega de portal por cliente\"", 1),
        ("Story 18h", "Indique o EON aos seus clientes", 0)]),
    ("Qua 02/12", "Planos e teste", [
        ("Story 10h", "Quanto custa emitir sem trava? R$ 4,66 por dia", 1), ("Feed 11h", "Plano EON: R$ 139,90/mês com teste grátis de 48 h", 1),
        ("Story 14h", "Pix ou cartão em até 12x", 0), ("Reel 17h", "EON: \"Testa 48 horas comigo, de graça\"", 1),
        ("Story 18h", "Perguntas frequentes no site", 0)]),
]

if __name__ == "__main__":
    tot = sum(len(d[2]) for d in DIAS)
    foco = sum(x[2] for d in DIAS for x in d[2])
    print(tot, foco, f"{foco / tot:.0%}")
