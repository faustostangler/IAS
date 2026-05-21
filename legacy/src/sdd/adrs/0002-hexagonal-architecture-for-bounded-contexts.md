# ADR 0002: Hexagonal Architecture for Bounded Contexts

## Status
🟢 CONFIRMADO

## Contexto
Each module in IAS (Media Ingestion, Speech Processing, etc.) must be protected from external framework changes (like swapping `yt-dlp` for a different extractor or Whisper for a cloud API). The business logic (Domain) should be the most stable part of the system.

## Decisão
We implemented **Hexagonal Architecture (Ports & Adapters)** within each module. 
- **Domain**: Contains pure logic and entities.
- **Application**: Contains Use Cases orchestrating the domain.
- **Infrastructure**: Contains Adapters implementing the Ports (Interfaces) defined by the domain.

## Alternativas consideradas
1. **Standard Layered Architecture (MVC)**: Rejected because it often couples the domain to the database or the web framework.
2. **Clean Architecture (Strict Version)**: Similar to Hexagonal, but Hexagonal was chosen for its clear focus on "Inside" (Domain) vs "Outside" (Infra) via explicit Ports.

## Consequências
- **Prós**: High testability (domain can be tested without infra), flexibility to swap technologies (adapters), clear separation of concerns.
- **Contras**: Higher initial boilerplate (multiple directories and interface definitions per module).
