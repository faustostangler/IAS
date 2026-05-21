# Shared Kernel, Implementation Tasks

## Prerequisites
- [ ] Dependencies: `pydantic`, `pydantic-settings`
- [ ] Environment file `.env` template defined

## Tasks

- [ ] T-01, Implement Centralized Configuration
  - Origin: `src/ias/config.py`
  - Definition of Done: `Settings` class implemented with Pydantic V2 and required defaults.
  - Confidence: 🟢

- [ ] T-02, Implement IASOrchestrator
  - Origin: `src/ias/shared_kernel/orchestrator.py`
  - Definition of Done: Sequential execution logic with fail-fast checks implemented.
  - Confidence: 🟢

- [ ] T-03, Implement Composition Root
  - Origin: `src/ias/main.py`
  - Definition of Done: `main()` function correctly initializes adapters and use cases, injecting them into the orchestrator.
  - Confidence: 🟢

## Test Tasks

- [ ] TT-01, Validate Full System Integration
  - Validates: `requirements.md` (Scenario: Full pipeline execution)
  - Method: End-to-end test with a real URL (or mocked adapters) covering the full chain.

- [ ] TT-02, Validate Fail-Fast Logic
  - Method: Force a failure in the Ingestion stage and verify that Transcription is never called.

## Suggested Order
1. **Config First**: T-01 is needed by all adapters.
2. **Orchestrator**: T-02 defines how everything fits.
3. **Main**: T-03 is the final glue.

## Pending Gaps (🔴)
- **Logging Refactor**: Plan to replace `print` with a structured `logger` (e.g., `structlog` or standard `logging`).
- **Idempotency**: Decide if re-running the same URL should skip ingestion/transcription if files already exist.
