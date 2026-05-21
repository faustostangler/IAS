# ADR 0006: Checkpointing and Resume Strategy

## Status
🟢 CONFIRMADO (Validado pelo usuário em `questions.md`)

## Contexto
The IAS pipeline consists of multiple heavy stages: Download -> Transcription -> Synthesis. A failure in any stage (network drop, crash, manual stop) currently requires restarting the entire process from the beginning, leading to wasted time and resources.

## Decisão
We decided to implement a **Checkpointing and Resume Strategy**. Each stage must verify the existence and validity of its expected input in the persistent storage before starting.
- **Ingestion**: Skip download if a valid audio file already exists for the given content reference.
- **Transcription**: Skip Whisper call if a valid transcript file already exists for the `MediaId`.
- **Synthesis**: Skip LLM call if the structured Knowledge Node already exists in the target vault (unless an update is explicitly requested).

## Alternativas consideradas
1. **Always Restart (Current)**: Rejected due to inefficiency.
2. **Database-Driven State**: Considered, but file-based checkpointing is sufficient and simpler for the current local-first architecture.

## Consequências
- **Prós**: Resilience to failures, significant reduction in re-processing time, better developer experience.
- **Contras**: Requires logic to handle stale or corrupted checkpoints.
