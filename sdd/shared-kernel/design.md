# Shared Kernel, Technical Design

## Interface

### Orchestrator: IASOrchestrator
| Symbol | Signature | Return | Observation |
| :--- | :--- | :--- | :--- |
| `IASOrchestrator.process_url` | `(url: str)` | `KnowledgeNode` | Main entry point for the full system workflow. |

### Configuration: Settings
| Symbol | Field | Type | Default |
| :--- | :--- | :--- | :--- |
| `Settings` | `STORAGE_PATH` | `str` | `./data` |
| `Settings` | `WHISPER_MODEL` | `str` | `base` |
| `Settings` | `LLM_MODEL` | `str` | `llama3` |

---

## Main Flow (The Pipeline)
1. **Receive URL**: `process_url` receives the input. `orchestrator.py:23` 🟢
2. **Ingest Stage**: Calls `self._ingest.execute(url)`. `orchestrator.py:28` 🟢
3. **Verify Ingest**: Checks if status is `COMPLETED`. If not, stops. `orchestrator.py:29` 🟢
4. **Transcribe Stage**: Calls `self._transcribe.execute(media.id, media.audio_path)`. `orchestrator.py:34` 🟢
5. **Verify Transcribe**: Checks if status is `COMPLETED`. If not, stops. `orchestrator.py:35` 🟢
6. **Compile Stage**: Calls `self._compile.execute(media.id, media.title, transcript.text)`. `orchestrator.py:40` 🟢
7. **Finalize**: Returns the compiled `KnowledgeNode`. `orchestrator.py:43` 🟢

## Dependencies
- **Pydantic Settings**: Used for strictly typed configuration validation and environment variable loading. 🟢
- **Module Use Cases**: Direct dependency on `IngestMediaUseCase`, `TranscribeAudioUseCase`, and `CompileKnowledgeUseCase`. 🟢

## Identified Design Decisions

| Decision | Evidence in Code | Confidence |
| :--- | :--- | :--- |
| **Manual DI** | Dependencies are injected via `__init__` without a DI framework. | `main.py:18` 🟢 |
| **Fail-Fast** | Pipeline aborts at the first non-completed stage. | `orchestrator.py:29` 🟢 |
| **Pydantic V2** | Leverages the latest Pydantic for validation and performance. | `config.py:1` 🟢 |

## Internal State
- The `orchestrator` is stateless; it only coordinates external components.
- The `settings` object is a singleton initialized at module load time.

## Observability
- **Stdout Logging**: Explicit `print` statements mark the start and failure/success of each phase. `orchestrator.py:27` 🟢

## Risks and Gaps
- 🟡 **Logging Level**: System uses `print` instead of a structured `logging` library, making it harder to capture telemetry in production environments.
- 🔴 **Transactionality**: There is no "rollback" logic. If compilation fails, the audio and transcript remain on disk but orphaned.
