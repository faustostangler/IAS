# Knowledge Compilation

## Overview
Responsible for transforming raw transcripts into structured, high-quality knowledge assets (Markdown nodes). It synthesizes information and ensures it is correctly persisted in the user's knowledge vault.

## Responsibilities
- Synthesize unstructured text into structured Markdown documents. 🟢
- Manage metadata and tags for the knowledge nodes. 🟢
- Persist nodes into a local file system (Obsidian Vault). 🟢
- Maintain compilation states (Pending, Compiling, Completed, Failed). 🟢

## Business Rules
- **Markdown Standardization**: All knowledge nodes must be saved as `.md` files. 🟢
- **Metadata Frontmatter**: Every node must include YAML frontmatter with `media_id` and `tags`. 🟢
- **Immutable Status**: Compilation status must strictly follow the domain state machine. 🟢
- **Local LLM usage**: Must use a local LLM adapter for privacy-preserving synthesis. 🟢
- **Text Chunking**: For transcripts exceeding LLM context limits, the system must implement a chunking/Map-Reduce strategy. 🔴 [Decisão User]
- **Update Policy**: If a node with the same title exists in the vault, it should be updated/overwritten with the new synthesis. 🔴 [Decisão User]

## Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| RF-01 | Knowledge Synthesis | Must | Given a transcript, the LLM generates a structured Markdown content. |
| RF-02 | Vault Persistence | Must | The system saves the generated content to the configured Obsidian vault path. |
| RF-03 | Sanitized Filenames | Should | Node titles must be sanitized to be safe for filenames (e.g., replacing `/`). |

## Non-Functional Requirements

| Type | Inferred Requirement | Evidence in Code | Confidence |
| :--- | :--- | :--- | :--- |
| Performance | Async IO | `adapters.py:27` (using `aiofiles`) | 🟢 |
| Integration | Local HTTP API | `adapters.py:43` (calling Ollama) | 🟢 |
| Reliability | Fault tolerance | `use_cases.py:38` | 🟢 |

## Acceptance Criteria

```gherkin
Scenario: Successful compilation
  Given a transcript for media "123" with title "Video Title"
  When the CompileKnowledgeUseCase is executed
  Then a KnowledgeNode is returned with status COMPLETED
  And a file named "Video Title.md" exists in the vault
  And the file contains valid YAML frontmatter

Scenario: Synthesis failure
  Given an unreachable local LLM service
  When the CompileKnowledgeUseCase is executed
  Then a KnowledgeNode is returned with status FAILED
```

## Priority (Moscow)

| Requirement | MoSCoW | Rationale |
| :--- | :--- | :--- |
| Vault Persistence | Must | Final goal of the entire system. |
| Knowledge Synthesis | Must | Core value added to the raw transcript. |
| Sanitized Filenames | Should | Prevents OS-level errors during save. |

## Code Traceability

| File | Function / Class | Coverage |
| :--- | :--- | :--- |
| `src/ias/modules/knowledge_compilation/domain/entities.py` | `KnowledgeNode`, `CompilationStatus` | 🟢 |
| `src/ias/modules/knowledge_compilation/application/use_cases.py` | `CompileKnowledgeUseCase` | 🟢 |
| `src/ias/modules/knowledge_compilation/infrastructure/adapters.py` | `ObsidianVaultRepository`, `OllamaSynthesizer` | 🟢 |
