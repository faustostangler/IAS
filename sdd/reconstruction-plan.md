# 🏗️ Plano de Reconstrução — IAS

> [!IMPORTANT]
> Este plano detalha a ordem de implementação para a reconstrução completa do sistema IAS, seguindo o paradigma **Modular Monolith + Hexagonal Architecture**.

## 📊 Status Geral
- **Progresso**: 0% (0/6 tarefas concluídas)
- **Fase Atual**: Planejamento Finalizado
- **Confiança das Specs**: 🟢 100% CONFIRMADO

---

## 🛠️ Alertas Pré-Voo
- **Hardware**: O servidor de reconstrução deve ter acesso a GPU para os testes do módulo `speech-processing` (Whisper).
- **Ollama**: O serviço Ollama deve estar rodando localmente para validar o módulo `knowledge-compilation`.
- **Ambiente**: Usar `uv` para gestão de dependências.

---

## 📋 Lista de Tarefas (Bottom-Up)

### 1. Shared Kernel: Foundation & Config
- **Objetivo**: Implementar a fundação do sistema (Configurações, Tipos Base, Exceções Globais).
- **Lê**: `sdd/shared-kernel/requirements.md`, `sdd/shared-kernel/design.md`, `sdd/shared-kernel/tasks.md`.
- **Pronto quando**: `Settings` valida `.env`, tipos de domínio base estão definidos e testados.
- **Status**: `pending`

### 2. Media Ingestion: YouTube Extraction
- **Objetivo**: Implementar o módulo de download e extração de áudio.
- **Lê**: `sdd/media-ingestion/requirements.md`, `sdd/media-ingestion/design.md`, `sdd/media-ingestion/tasks.md`.
- **Pronto quando**: `YoutubeAudioExtractor` baixa áudio via URL e salva com ID UUID interno.
- **Status**: `pending`

### 3. Speech Processing: AI Transcription
- **Objetivo**: Implementar a transformação de áudio em texto via Whisper.
- **Lê**: `sdd/speech-processing/requirements.md`, `sdd/speech-processing/design.md`, `sdd/speech-processing/tasks.md`.
- **Pronto quando**: `WhisperSpeechProcessor` gera transcrição correta e respeita o checkpoint (pula se já existe).
- **Status**: `pending`

### 4. Knowledge Compilation: Synthesis (Map-Reduce)
- **Objetivo**: Implementar a síntese de conhecimento e persistência no Vault.
- **Lê**: `sdd/knowledge-compilation/requirements.md`, `sdd/knowledge-compilation/design.md`, `sdd/knowledge-compilation/tasks.md`.
- **Pronto quando**: Implementado Map-Reduce para textos longos; arquivos no Vault são atualizados sem perda de metadados.
- **Status**: `pending`

### 5. Orchestration: Sequential Pipeline
- **Objetivo**: Unificar os módulos sob o orquestrador com fila sequencial.
- **Lê**: `sdd/shared-kernel/design.md` (Seção Orchestrator), `sdd/adrs/0005-sequential-processing-queue.md`.
- **Pronto quando**: Pipeline executa sequencialmente; segunda requisição aguarda a primeira sem estourar VRAM.
- **Status**: `pending`

### 6. Presentation Layer: CLI & API
- **Objetivo**: Expor o sistema via linha de comando e REST API.
- **Lê**: `sdd/openapi/ias-api.yaml`, `sdd/user-stories/process-youtube-to-vault.md`.
- **Pronto quando**: `ias <url>` e `POST /process` funcionam de ponta a ponta.
- **Status**: `pending`

---
*Gerado pelo **Reconstructor** em 2026-05-12.*
