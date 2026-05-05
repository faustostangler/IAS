# Knowledge Compilation, Implementation Tasks

## Prerequisites
- [ ] Dependencies: `httpx`, `aiofiles`
- [ ] Running Ollama instance with desired model pulled (e.g., `llama3`)

## Tasks

- [ ] T-01, Define Knowledge Compilation Domain
  - Origin: `src/ias/modules/knowledge_compilation/domain/entities.py`
  - Definition of Done: `KnowledgeNode` and `CompilationStatus` implemented.
  - Confidence: 🟢

- [ ] T-02, Define Compilation Ports
  - Origin: `src/ias/modules/knowledge_compilation/domain/ports.py`
  - Definition of Done: Interfaces for `KnowledgeSynthesizerPort` and `VaultRepositoryPort` defined.
  - Confidence: 🟢

- [ ] T-03, Implement CompileKnowledgeUseCase
  - Origin: `src/ias/modules/knowledge_compilation/application/use_cases.py`
  - Definition of Done: Orchestration between synthesis, persistence, and state transitions implemented.
  - Confidence: 🟢

- [ ] T-04, Implement OllamaSynthesizer Adapter
  - Origin: `src/ias/modules/knowledge_compilation/infrastructure/adapters.py`
  - Definition of Done: Integration with Ollama API using `httpx`.
  - Confidence: 🟢

- [ ] T-05, Implement ObsidianVaultRepository Adapter
  - Origin: `src/ias/modules/knowledge_compilation/infrastructure/adapters.py`
  - Definition of Done: Async file operations and Markdown/YAML formatting implemented.
  - Confidence: 🟢

## Test Tasks

- [ ] TT-01, Validate Full Synthesis and Save Cycle
  - Validates: `requirements.md` (Scenario: Successful compilation)
  - Method: Integration test with a mocked Ollama response and verification of file existence.

- [ ] TT-02, Validate Filename Sanitization
  - Validates: `requirements.md` (RF-03)
  - Method: Unit test for `ObsidianVaultRepository` with a title containing slashes.

## Suggested Order
1. **Domain**: (T-01, T-02)
2. **Infrastructure**: (T-05) - Test saving first as it's simpler.
3. **Infrastructure**: (T-04) - Requires Ollama environment.
4. **Application**: (T-03)

## Pending Gaps (🔴)
- **Retry Mechanism**: No automatic retry for transient LLM API failures.
- **Overwrite Protection**: Decide if we should append, version, or block overwriting existing notes.
