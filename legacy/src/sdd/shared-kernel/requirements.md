# Shared Kernel

## Overview
Provides common abstractions, orchestration logic, and centralized configuration used across all Bounded Contexts of the Intelligent Audio Scriber. It ensures consistency and enables cross-module coordination.

## Responsibilities
- Centralize system-wide configurations and fail-fast validation. 🟢
- Orchestrate the sequential execution of the media-to-knowledge pipeline. 🟢
- Provide a composition root for Dependency Injection. 🟢
- Handle shared logging and status reporting (informal). 🟡

## Business Rules
- **Sequential Pipeline Integrity**: The pipeline must stop immediately if any stage fails. 🟢
- **Configuration Validation**: The system must fail-fast during startup if required environment variables are missing or invalid. 🟢
- **Coupling Control**: Modules must not depend on each other directly; they interact through the shared orchestrator and domain entities. 🟢
- **Sequential Queue**: The system must process only one URL at a time to ensure hardware (VRAM) stability. 🔴 [Decisão User]

## Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| RF-01 | Pipeline Orchestration | Must | Given a URL, the system executes Ingestion, Transcription, and Compilation in order. |
| RF-02 | Centralized Configuration | Must | All modules use a single source of truth for settings (Storage path, Model names). |
| RF-03 | Status Reporting | Should | The system provides console output for each major stage of the process. |

## Non-Functional Requirements

| Type | Inferred Requirement | Evidence in Code | Confidence |
| :--- | :--- | :--- | :--- |
| Architecture | Modular Monolith Pattern | `orchestrator.py:10` | 🟢 |
| Robustness | Fail-fast validation | `config.py:5` (Pydantic) | 🟢 |
| Extensibility | Dependency Injection ready | `orchestrator.py:13` | 🟢 |

## Acceptance Criteria

```gherkin
Scenario: Full pipeline execution
  Given a valid YouTube URL
  When process_url is called
  Then Ingestion is triggered
  And Transcription starts only after Ingestion completes
  And Compilation starts only after Transcription completes
  And a success message is printed at the end
```

## Priority (Moscow)

| Requirement | MoSCoW | Rationale |
| :--- | :--- | :--- |
| Pipeline Orchestration | Must | The core engine that ties everything together. |
| Configuration Validation | Must | Ensures the system is correctly configured before wasting resources on AI tasks. |

## Code Traceability

| File | Function / Class | Coverage |
| :--- | :--- | :--- |
| `src/ias/shared_kernel/orchestrator.py` | `IASOrchestrator` | 🟢 |
| `src/ias/config.py` | `Settings` | 🟢 |
| `src/ias/main.py` | `main` (Composition Root) | 🟢 |
