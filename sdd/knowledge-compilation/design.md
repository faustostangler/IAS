# Knowledge Compilation, Technical Design

## Interface

### Use Case: CompileKnowledgeUseCase
| Symbol | Signature | Return | Observation |
| :--- | :--- | :--- | :--- |
| `CompileKnowledgeUseCase.execute` | `(media_id: str, title: str, transcript_text: str)` | `KnowledgeNode` | Async entry point for the compilation pipeline. |

### Domain Ports
| Symbol | Signature | Return | Observation |
| :--- | :--- | :--- | :--- |
| `KnowledgeSynthesizerPort.synthesize` | `(title: str, transcript: str)` | `str` | Interface for AI synthesis. |
| `VaultRepositoryPort.save` | `(node: KnowledgeNode)` | `None` | Interface for node persistence. |

### Infrastructure Adapters
| Symbol | Signature | Return | Observation |
| :--- | :--- | :--- | :--- |
| `OllamaSynthesizer.synthesize` | `(title: str, transcript: str)` | `str` | Implementation using local Ollama HTTP API. |
| `ObsidianVaultRepository.save` | `(node: KnowledgeNode)` | `None` | Implementation using `aiofiles` for MD storage. |

---

## Main Flow
1. **Initiation**: `CompileKnowledgeUseCase` receives media data and transcript. `use_cases.py:15` 🟢
2. **Entity Creation**: `KnowledgeNode` initialized in `PENDING` state. `use_cases.py:18` 🟢
3. **Synthesis Start**: Status updated to `COMPILING`. `use_cases.py:25` 🟢
4. **Text Chunking**: If transcript length exceeds threshold, text is split into manageable chunks. 🔴 [Decisão User]
5. **AI Generation**: `OllamaSynthesizer` sends prompts for each chunk or full text to Ollama. `adapters.py:61` 🟢
5. **Entity Update**: Node is updated with synthesized content and moves to `COMPLETED`. `use_cases.py:32` 🟢
6. **Persistence**: `ObsidianVaultRepository` formats the node with frontmatter and writes to disk. `adapters.py:17` 🟢

## Alternative Flows
- **Synthesis Failure**: If Ollama is down or returns an error, status moves to `FAILED`. `use_cases.py:38` 🟢
- **Filename Sanitization**: Slashes in titles are replaced with dashes before saving. `adapters.py:21` 🟢

## Dependencies
- **httpx**: Used for communication with the Ollama service. 🟢
- **aiofiles**: Used for non-blocking Markdown file creation. 🟢
- **pydantic-settings**: Provides vault path configuration. 🟢

## Identified Design Decisions

| Decision | Evidence in Code | Confidence |
| :--- | :--- | :--- |
| **Separation of Ports** | Synthesis (compute) and Persistence (storage) are distinct ports. | 🟢 |
| **Structured Prompting** | System uses a specific prompt template for synthesis. | `adapters.py:51` 🟢 |
| **YAML Frontmatter** | Metadata is standardized at the top of the MD file. | `adapters.py:32` 🟢 |

## Internal State
The `KnowledgeNode` entity maintains:
- `id`: Unique node identifier.
- `media_id`: Link to source media.
- `title`: Document title.
- `content`: Synthesized text.
- `tags`: Metadata tags.
- `status`: `PENDING`, `COMPILING`, `COMPLETED`, `FAILED`.

## Observability
- **HTTP Tracking**: Errors during Ollama calls are raised via `response.raise_for_status()`. `adapters.py:69` 🟢

## Risks and Gaps
- 🟡 **Ollama Availability**: The system assumes Ollama is running on localhost; no healthcheck or dynamic discovery.
- 🔴 **Token Limits**: Very long transcripts might exceed LLM context windows (no chunking logic observed).
- 🔴 **Vault Conflict**: No logic to handle existing files with the same name (will be overwritten).
