# Guia de continuidade: marketing do EON no Instagram

Este guia passa o trabalho do Instagram **@eonsistema** para uma conversa nova, separada do desenvolvimento do ERP.
Quem continuar deve ler este arquivo inteiro antes de produzir ou agendar qualquer coisa.

## 1. Situação em 06/11/2026

- O primeiro ciclo está **todo agendado no Metricool**: 60 publicações de 06/11 a 02/12/2026.
- As 5 publicações de 06/11 saíram (conferido às 18h20). Uma delas é o reel https://www.instagram.com/reel/Dfaa6L0lX2d/
- Erick aprovou o plano inteiro e a voz do Caio no ritmo "alegre". Não é preciso pedir aprovação peça por peça dentro do plano já aprovado.
  Conteúdo novo (um novo mês, temas novos) segue para aprovação antes de ser agendado.

## 2. Contas e ferramentas

| O quê | Detalhe |
|---|---|
| Instagram | @eonsistema (conta profissional, sem página no Facebook) |
| Metricool | marca **blogId / brandId 7918535**, fuso `America/Fortaleza`, só o Instagram conectado |
| Hospedagem das mídias | este repositório (público). O Metricool baixa de `https://raw.githubusercontent.com/erickoliveiracontabil-web/eon-instagram/main/<dia>/<arquivo>` e guarda cópia própria |
| Voz | **Speko** (conector do Claude): provedor `azure:MAI-Voice-2.1`, voz `pt-BR-Caio:MAI-Voice-2.1`. Crédito de US$ 10; o primeiro ciclo gastou cerca de US$ 0,15 |
| ElevenLabs | conectado, mas a geração gratuita estava ocupada no teste. Não está em uso |

O repositório é público. Nele entram **só** artes, vídeos, locuções e as ferramentas de geração.
Nunca entram código do ERP, dados de clientes, senhas, chaves ou CPF.

## 3. Rotina de publicação (aprovada pelo Erick)

- **Dias:** sexta, segunda e quarta.
- **Por dia, 5 publicações:**
  - stories às **10h**, **14h** e **18h**;
  - **1 post no feed às 11h**;
  - **1 reel às 17h**.
- **Foco das primeiras semanas:** cerca de **50%** das publicações (de qualquer tipo) mostram que o EON emite **NF-e e NFS-e sem as travas dos portais do governo**.
  No primeiro ciclo foram 32 de 60.
- **Mascote:** aparece em todos os reels e em alguns stories. Fica fora da maioria dos posts de feed.
- **Tom:** orgânico, próximo e descontraído. As legendas terminam com "Teste grátis por 48 horas: link na bio." e hashtags curtas com #eonsistema.
- **Horários:** vieram do melhor horário do Metricool (pico às 10h nos dias úteis e às 18h).
  A partir da 3ª semana já dá para ajustar pelos números reais da conta.

### Stories com adesivo (enquete, caixinha, link)

O agendamento não consegue colocar adesivos. Esses stories são agendados com `autoPublish: false`.
O Metricool avisa no celular do Erick, e ele põe o adesivo e publica.
Datas no ciclo 1:

- enquete às 10h: 09/11, 16/11, 23/11 e 30/11;
- caixinha às 18h: 11/11 e 27/11.

## 4. O que pode ser afirmado (conferido no código do EON)

**Pode:**
- emite NF-e, NFC-e e NFS-e de dentro do sistema;
- confere os dados antes do envio e explica a rejeição em português;
- funciona no navegador do celular, sem instalar nada;
- avisa no Início quando o certificado A1 está perto de vencer;
- avisa quando o estoque fica abaixo do mínimo, e a nota emitida baixa o estoque;
- NFC-e em contingência quando a Sefaz cai;
- painel do contador com download dos XMLs dos clientes;
- NFS-e enviada por e-mail ao tomador;
- teste grátis de 48 h;
- planos "a partir de R$ 139,90/mês";
- Pix ou cartão em até 12x;
- suporte por WhatsApp.

**Não afirmar sem conferir antes:**
- envio do DANFE pelo WhatsApp;
- "notas ilimitadas";
- quais módulos o plano básico inclui (há módulos avulsos);
- qualquer número de clientes ou depoimento.

As telas usadas nas artes são da empresa fictícia de demonstração.

## 5. Como produzir

Requisitos: Python 3, Playwright com Chromium, Pillow, numpy e ffmpeg.
Rode tudo a partir da raiz do repositório.

### Artes estáticas

- `ferramentas/modelos.py` tem os moldes:
  - `f_titulo`, `f_ponto`, `f_tela`, `f_celular` para o feed em 4:5 (1080×1350);
  - `s_texto`, `s_tela` para stories em 9:16 (1080×1920).
- Use `*texto*` para destacar em verde.
- `ferramentas/pecas.py`: `render({nome: html}, pasta)` gera os JPGs.
- `ferramentas/produzir.py` tem o ciclo 1 inteiro (dicionário `DIAS`, com artes, legendas e falas dos reels). Use como modelo para o próximo mês.
- `ferramentas/plano.py` e `ferramentas/cal2.py` geram a imagem do calendário. O Erick prefere ver o material em **imagens e telas**, não em links.

### Reels com o mascote falando

1. **Escreva as falas.** São 4 frases curtas por reel; a última termina em "Bora testar?".
2. **Gere a locução** com o Speko `audio.synthesize`, num texto só por reel:

   ```json
   {"text": "...", "intent": {"language": "pt-BR", "optimizeFor": "accuracy"},
    "voice": "pt-BR-Caio:MAI-Voice-2.1", "speed": 1.3,
    "instructions": "Fale rápido, de forma alegre, descontraída e cheia de energia, com um sorriso na voz, como um mascote animado conversando com o público num reel de Instagram. Sem pausas longas.",
    "constraints": {"allowedProviders": {"tts": ["azure:MAI-Voice-2.1"]}}}
   ```

   **Pronúncia** (escreva assim no texto da voz, não na tela):

   | Na tela | Na voz |
   |---|---|
   | EON | **Íon** |
   | NF-e | ene-éfe-é |
   | NFS-e | ene-éfe-ésse-é |
   | NFC-e | ene-éfe-cê-é |
   | XML | xis-eme-ele |
   | 48 | quarenta e oito |
   | R$ 139,90 | cento e trinta e nove e noventa |

3. **Salve o áudio.** O resultado vem grande e é salvo em arquivo.
   Converta com `python3 -I ferramentas/decod.py <arquivo_resultado> <saida.wav>` e grave em `locucao/<dia>.mp3`.
4. **Confira.** Transcreva com o Speko `audio.transcribe` (`language: pt-BR`, `word_timestamps: true`) a partir da URL raw do mp3.
   Verifique a pronúncia das siglas e se não há silêncio longo no meio. Já aconteceu uma locução com 9 s de silêncio.
5. **Monte o vídeo** com `python3 ferramentas/montar_reels.py <dia>`, que gera `<dia>/reel_alegre.mp4`.
   - A fala é acelerada em 1,22 com `atempo`, sem afinar a voz.
   - As pausas internas ficam em no máximo 0,16 s.
   - O áudio é dividido em uma parte por balão, pela proporção de letras de cada fala.
   - O mascote se move suave, pelo volume da voz, sem tremer.
   - Cada reel deve ter **mais de 8 s**. No ciclo 1 ficaram entre 11 e 17 s.

### Agendar no Metricool

- Faça commit e push das mídias em `<AAAA-MM-DD>/` e agende com `createScheduledPost`.
- **Story:** `instagramData.type = STORY`, sem texto.
- **Feed:** `POST`; o carrossel leva várias URLs em `media`.
- **Reel:** `REEL`, `showReelOnFeed: true`, `videoCoverMilliseconds: 4000`.
- Para trocar a mídia de um post já agendado, use `updateScheduledPost` (o id muda e o uuid fica). Use um **nome de arquivo novo**, porque o Metricool guarda cópia e o cache do GitHub demora.
- No fim do dia, confira com `getScheduledPosts`: o status deve ser `PUBLISHED`.

## 6. Próximos passos sugeridos

- Por volta de 25/11, puxar os números do Metricool (alcance e engajamento por formato e horário) e propor o ciclo 2, de 04/12 em diante, para aprovação.
- Pendências mencionadas pelo Erick:
  - página no Facebook: não existe, e só é necessária para usar músicas do Instagram via API;
  - Perfil da Empresa no Google: pode ser conectado no Metricool.
