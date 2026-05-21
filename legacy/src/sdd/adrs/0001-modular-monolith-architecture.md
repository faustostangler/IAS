# ADR 0001: Modular Monolith Architecture

## Status
🟢 CONFIRMADO (Inferido da estrutura do projeto)

## Contexto
The system needs to manage complex workflows involving media ingestion, speech processing, and knowledge compilation. While these are distinct domains, the operational overhead of managing multiple microservices (deployment, networking, distributed tracing) is high for a tool that is currently focused on local-first processing and fast iteration.

## Decisão
We adopted a **Modular Monolith** architecture. The codebase is organized into clear Bounded Contexts (modules) that are logically separated but reside within a single deployable unit.

## Alternativas consideradas
1. **Microservices**: Rejected due to premature complexity and overhead for a single-user system.
2. **Traditional Monolith (Layered)**: Rejected because it leads to "Big Ball of Mud" where domain boundaries are blurred, making it hard to extract modules later if needed.

## Consequências
- **Prós**: Simplified deployment (single source of truth), reduced latency between modules, easier refactoring within the same repository.
- **Contras**: Risk of circular dependencies if shared kernel is not strictly managed; scales as a single unit (cannot scale just the speech processing module independently).
