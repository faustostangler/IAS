# Media Ingestion, Technical Design

## Interface

### Use Case: IngestMediaUseCase
| Symbol | Signature | Return | Observation |
| :--- | :--- | :--- | :--- |
| `IngestMediaUseCase.execute` | `(url: str)` | `MediaSource` | Async method that orchestrates the ingestion. |

### Domain Port: AudioExtractorPort
| Symbol | Signature | Return | Observation |
| :--- | :--- | :--- | :--- |
| `AudioExtractorPort.extract_audio` | `(source: MediaSource)` | `MediaSource` | Abstract contract for extraction. |

### Infrastructure Adapter: YoutubeAudioExtractor
| Symbol | Signature | Return | Observation |
| :--- | :--- | :--- | :--- |
| `YoutubeAudioExtractor.extract_audio` | `(source: MediaSource)` | `MediaSource` | Implements the port using `yt-dlp`. |
| `YoutubeAudioExtractor._download` | `(opts: dict, url: str)` | `dict` | Internal helper for `YoutubeDL` calls. |

---

## Main Flow
1. **Initiation**: `IngestMediaUseCase` receives a URL and generates a `MediaId` (UUID v4). The domain operates exclusively on this internal ID. `use_cases.py:16` 🟢
2. **Checkpoint Check**: System checks if an audio file associated with the source already exists in storage. 🔴 [Decisão User]
3. **Entity Creation**: A `MediaSource` entity is initialized in `PENDING` state. `use_cases.py:17` 🟢
3. **Status Update**: Entity state changes to `PROCESSING`. `use_cases.py:20` 🟢
4. **Extraction Delegation**: The use case calls `_audio_extractor.extract_audio(source)`. `use_cases.py:24` 🟢
5. **Worker Execution**: The adapter runs `yt-dlp` in a separate thread using `run_in_executor` to avoid blocking the async loop. `adapters.py:37` 🟢
6. **Persistence**: Audio is downloaded to `STORAGE_PATH/audio/` using the YouTube ID as filename. `adapters.py:29` 🟢
7. **Completion**: The adapter updates the entity with the video title and final `audio_path`, setting status to `COMPLETED`. `adapters.py:42` 🟢

## Alternative Flows
- **Extraction Error**: If `yt-dlp` fails (invalid URL, network error), the use case catches the exception and returns the entity in `FAILED` state. `use_cases.py:27` 🟢
- **Lazy Initialization**: `YoutubeAudioExtractor` ensures the output directory exists upon initialization. `adapters.py:16` 🟢

## Dependencies
- **yt-dlp**: External library used for downloading and extracting media information. 🟢
- **asyncio**: Used for managing the non-blocking execution of the download worker. 🟢
- **uuid**: Used for unique ID generation. 🟢

## Identified Design Decisions

| Decision | Evidence in Code | Confidence |
| :--- | :--- | :--- |
| **Hexagonal Architecture** | Strict separation between Port (domain) and Adapter (infra). | 🟢 |
| **Thread Offloading** | Use of `run_in_executor` for CPU/IO heavy tasks (yt-dlp). | 🟢 |
| **Immutable Entities** | State transitions return new `MediaSource` instances. | 🟢 |
| **MP3 Standardization** | yt-dlp post-processor fixed to `mp3` at `192kbps`. | 🟢 |

## Internal State
The `MediaSource` entity maintains:
- `id`: Unique identifier.
- `url`: Source URL.
- `status`: One of `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`.
- `title`: Video title (populated after extraction).
- `audio_path`: Local path to the .mp3 file.

## Observability
- **Standard Output**: The `IASOrchestrator` prints status messages to stdout during ingestion. `orchestrator.py:27` 🟢
- **Error Handling**: Exceptions are caught but not currently logged with detailed stack traces in the use case level. 🟡

## Risks and Gaps
- 🔴 **URL Validation**: The code doesn't perform domain-specific validation (e.g., checking if it's actually a YouTube URL) before passing it to `yt-dlp`.
- 🟡 **Concurrency Limit**: There is no explicit limit on concurrent downloads in the `YoutubeAudioExtractor`.
