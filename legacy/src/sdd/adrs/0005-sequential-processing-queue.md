# ADR 0005: Strict Sequential Processing Queue

## Status
🟢 CONFIRMADO (Validado pelo usuário em `questions.md`)

## Contexto
Media processing (Whisper transcription) and Knowledge Synthesis (LLM/Ollama) are highly resource-intensive operations, primarily utilizing VRAM and GPU cycles. Concurrent execution of these tasks can lead to "Out of Memory" (OOM) errors and system instability, especially on local consumer hardware.

## Decisão
We adopted a **Strict Sequential Processing Queue**. The system will process only one ingestion/synthesis request at a time. New requests will be queued and executed in order, ensuring that only one instance of the heavy models is active or loaded into memory at any given moment.

## Alternativas consideradas
1. **Parallel Processing**: Rejected to avoid hardware resource exhaustion.
2. **Resource-Based Scaling**: Considered (loading/unloading based on available VRAM), but deemed too complex for the current stage.

## Consequências
- **Prós**: Deterministic resource usage, avoids OOM errors, simpler state management.
- **Contras**: Increased waiting time for users when multiple requests are submitted simultaneously.
