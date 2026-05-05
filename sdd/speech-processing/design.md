# Speech Processing, Technical Design

## Interface

### Use Case: TranscribeAudioUseCase
| Symbol | Signature | Return | Observation |
| :--- | :--- | :--- | :--- |
| `TranscribeAudioUseCase.execute` | `(media_id: str, audio_path: str)` | `SpeechTranscript` | Async entry point for the transcription workflow. |

### Domain Port: SpeechProcessorPort
| Symbol | Signature | Return | Observation |
| :--- | :--- | :--- | :--- |
| `SpeechProcessorPort.transcribe` | `(transcript: SpeechTranscript)` | `SpeechTranscript` | Contract for the AI transcription adapter. |

### Infrastructure Adapter: WhisperSpeechProcessor
| Symbol | Signature | Return | Observation |
| :--- | :--- | :--- | :--- |
| `WhisperSpeechProcessor.transcribe` | `(transcript: SpeechTranscript)` | `SpeechTranscript` | Implementation using `openai-whisper`. |

---

## Main Flow
1. **Initiation**: `TranscribeAudioUseCase` receives `media_id` and `audio_path`. `use_cases.py:14` 🟢
2. **Entity Initialization**: Creates `SpeechTranscript` in `PENDING` state. `use_cases.py:17` 🟢
3. **Status Change**: Moves entity to `PROCESSING`. `use_cases.py:24` 🟢
4. **Lazy Loading**: `WhisperSpeechProcessor` loads the Whisper model into memory/VRAM only on the first call. `adapters.py:24` 🟢
5. **Worker Execution**: Calls `model.transcribe` inside a `run_in_executor` block to prevent blocking the async loop. `adapters.py:28` 🟢
6. **Completion**: Updates the entity with transcribed text and sets status to `COMPLETED`. `adapters.py:31` 🟢

## Alternative Flows
- **Processing Exception**: Any error during transcription (OOM, missing file) triggers the `fail()` transition. `use_cases.py:31` 🟢

## Dependencies
- **openai-whisper**: The core AI library for speech-to-text. 🟢
- **torch**: Backend for Whisper model execution. 🟢
- **asyncio**: Orchestrates non-blocking model inference. 🟢

## Identified Design Decisions

| Decision | Evidence in Code | Confidence |
| :--- | :--- | :--- |
| **Lazy Loading** | Model is not loaded until the first `transcribe` call. | 🟢 |
| **Thread Offloading** | Use of `run_in_executor` for CPU/GPU intensive tasks. | 🟢 |
| **Domain Isolation** | Use case only knows about the Port, not Whisper specifics. | 🟢 |

## Internal State
The `SpeechTranscript` entity maintains:
- `id`: Unique transcript identifier.
- `media_id`: Link to the source media.
- `audio_path`: Path used for processing.
- `text`: Resulting transcription string.
- `status`: `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`.

## Observability
- **Status Printing**: Monitored by the `IASOrchestrator`. `orchestrator.py:33` 🟢

## Risks and Gaps
- 🟡 **VRAM Management**: Multiple concurrent requests could lead to `Out of Memory` errors as there is no request queuing mechanism.
- 🔴 **Long Audio Support**: No logic for chunking or progress reporting for very long files.
