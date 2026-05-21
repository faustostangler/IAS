# ADR 0007: Synthesis Chunking and Map-Reduce Strategy

## Status
🟢 CONFIRMADO (Validado pelo usuário em `questions.md`)

## Contexto
Local LLMs (e.g., Llama 3 via Ollama) have finite context windows. Transcripts from long videos (30+ minutes) easily exceed these limits, causing the model to lose information or fail to generate a coherent synthesis.

## Decisão
We decided to adopt a **Map-Reduce / Chunking Strategy** for synthesis. 
1. **Map Phase**: Divide the long transcript into logical chunks (based on time or word count) and synthesize each chunk independently.
2. **Reduce Phase**: Aggregate the partial syntheses and perform a final consolidation into a single high-quality Knowledge Node.

## Alternativas consideradas
1. **Truncation**: Rejected as it leads to information loss.
2. **Infinite Context Models**: Rejected due to lack of local hardware support for extremely large context windows.

## Consequências
- **Prós**: Support for arbitrary length audio processing, more granular knowledge extraction.
- **Contras**: Increased processing time (multiple LLM calls), higher complexity in the Orchestration layer.
