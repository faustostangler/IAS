# 🔴 Reversa: Questões de Validação Técnica

Fausto, encontrei os seguintes pontos que precisam da sua validação para fechar o SDD com 100% de confiança. Por favor, preencha o campo **Resposta** de cada item.

---

## 1. Identidade de Entidades (ID Strategy)

**Contexto**: No módulo `media-ingestion`, a spec menciona geração de UUID v4 para `MediaId`, mas o contrato de armazenamento (`contracts.md`) diz que o nome do arquivo é o ID do YouTube.
**Pergunta**: Qual é a estratégia oficial de ID? 
- A) O `MediaId` é o ID do YouTube (ex: `aqz-KE-BPKQ`)
- B) O `MediaId` é um UUID v4 interno, e o ID do YouTube é guardado apenas como metadado/referência?

**Resposta**: UUID v4 interno, domain não toca na url. 

---

## 2. Persistência e Resiliência (Checkpoints)

**Contexto**: O sistema orquestra três etapas pesadas (Download -> Transcrição -> Síntese). Atualmente, se o processo cair no meio, não parece haver lógica de "resume" ou banco de dados para salvar o estado parcial.
**Pergunta**: Para a reimplementação, devemos considerar:
- A) Manter o comportamento atual (Monolito In-Memory, se cair reinicia do zero).
- B) Adicionar um requisito de "Checkpointing" (verificar se o áudio/transcrição já existe no disco antes de processar).

**Resposta**: B

---

## 3. Limites de Contexto (LLM)

**Contexto**: Transcrições de vídeos longos podem exceder o limite de tokens do Ollama/Llama3. Não encontrei lógica de chunking (divisão de texto) no código atual.
**Pergunta**: Como o sistema deve lidar com vídeos muito longos?
- A) Erro simples (Out of Context).
- B) Requisito de implementação de "Map-Reduce" ou "Chunking" para síntese de textos longos.

**Resposta**: B

---

## 4. Concorrência e Hardware

**Contexto**: O processamento de áudio (Whisper) e síntese (Ollama) são intensivos em GPU/VRAM.
**Pergunta**: O sistema deve suportar processamento paralelo de múltiplas URLs ou deve garantir uma fila sequencial estrita (1 por vez) para evitar estouro de memória?

**Resposta**: Fila sequencial estrita.

---

## 5. Destino do Vault (Obsidian)

**Contexto**: Se já existir um arquivo com o mesmo título no Vault, o sistema atualmente sobrescreve (`aiofiles.open('w')`).
**Pergunta**: Qual o comportamento desejado para conflitos?
- A) Sobrescrever (Atual).
- B) Renomear (ex: `Titulo (1).md`).
- C) Abortar/Avisar.

**Resposta**: Editar e atualizar (sobrescrever com edição)

---

💡 **Instruções**: Após preencher as respostas acima, salve este arquivo e digite `reversa` no chat para eu processar as definições e atualizar as specs in-place.
