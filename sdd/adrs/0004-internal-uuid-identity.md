# ADR 0004: Internal UUID for Domain Identity

## Status
🟢 CONFIRMADO (Validado pelo usuário em `questions.md`)

## Contexto
The system interacts with external sources (YouTube) that provide their own identifiers (e.g., `aqz-KE-BPKQ`). Relying on these external IDs as primary keys within the internal domain creates tight coupling and potential issues if a video is re-uploaded or if the system scales to other media sources.

## Decisão
We decided to use **Internal UUID v4** as the primary identity (`MediaId`) for all domain entities. 
The external ID (YouTube ID) is treated as secondary metadata (reference) and is not used to identify the entity within the business logic or as the primary key in the storage layer.

## Alternativas consideradas
1. **Natural IDs (YouTube ID)**: Rejected because it couples the system to a specific external provider.
2. **Deterministic UUIDs (Name-based)**: Considered, but random UUID v4 provides better separation and avoids collisions if the same content is ingested from different platforms.

## Consequências
- **Prós**: High cohesion, isolation from external ID changes, easier integration with future non-YouTube sources.
- **Contras**: Requires a mapping between internal IDs and external references for debugging and reporting.
