# ADR 0003: Local-First AI Processing

## Status
🟢 CONFIRMADO

## Contexto
Audio transcription and knowledge synthesis can be expensive and raise privacy concerns when using public cloud APIs. For a developer/personal productivity tool, low latency and offline availability are key features.

## Decisão
The system is designed with a **Local-First** approach for AI processing. Default adapters use:
- **OpenAI Whisper** (local execution via `openai-whisper` and `torch`).
- **Ollama** (local LLM execution) for synthesis.

## Alternativas consideradas
1. **Cloud-Native (OpenAI/Anthropic API)**: Rejected as default due to cost and dependency on internet/external tokens.
2. **Hybrid**: Not implemented yet, but the Hexagonal structure allows adding Cloud Adapters later.

## Consequências
- **Prós**: Zero per-request cost, full privacy, works offline, leverages user's hardware (GPU).
- **Contras**: High initial hardware requirements (RAM/VRAM), slower processing on low-end machines compared to high-end cloud clusters.
