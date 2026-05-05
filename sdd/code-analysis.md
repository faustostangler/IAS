# Code Analysis - IAS

## 🏗️ Architecture Overview
The system is built as a **Modular Monolith** following **Hexagonal Architecture** (Ports & Adapters) and **Domain-Driven Design (DDD)** principles.

### Modules (Bounded Contexts)
1.  **MediaIngestion**: Handles URL validation and audio extraction using `yt-dlp`.
2.  **SpeechProcessing**: Handles local transcription using `OpenAI Whisper`.
3.  **KnowledgeCompilation**: Handles LLM-based synthesis (via `Ollama`) and vault persistence (Obsidian).

---

## 🛠️ Module Breakdown

### 1. MediaIngestion
-   **Pattern**: Hexagonal Architecture.
-   **Core Logic**: `IngestMediaUseCase` coordinates the process. It uses `YoutubeAudioExtractor` as an infrastructure adapter.
-   **Key Algorithms**:
    -   `yt-dlp` integration for high-fidelity audio extraction.
    -   Post-processing logic to convert extraction info into `MediaSource` domain entity.
-   **Error Handling**: Domain entity transitions to `MediaStatus.FAILED` on any extraction error.

### 2. SpeechProcessing
-   **Pattern**: Hexagonal Architecture.
-   **Core Logic**: `TranscribeAudioUseCase` manages the transcription lifecycle.
-   **Key Algorithms**:
    -   Lazy loading of Whisper model in `WhisperSpeechProcessor`.
    -   Async execution of GPU-bound `whisper.transcribe` using `run_in_executor` to prevent blocking the event loop.
-   **Error Handling**: Transitions to `SpeechStatus.FAILED` on transcription errors.

### 3. KnowledgeCompilation
-   **Pattern**: Hexagonal Architecture.
-   **Core Logic**: `CompileKnowledgeUseCase` synthesizes and persists the final output.
-   **Key Algorithms**:
    -   Prompt engineering for structured Markdown generation via `OllamaSynthesizer`.
    -   Obsidian-compatible metadata (YAML frontmatter) generation in `ObsidianVaultRepository`.
    -   Async file I/O using `aiofiles`.

---

## 🚦 Control Flow & Orchestration
The `IASOrchestrator` in `shared_kernel` manages the sequential execution of the pipeline:
1.  `MediaIngestion.execute(url)` -> `MediaSource`
2.  `SpeechProcessing.execute(media_id, audio_path)` -> `SpeechTranscript`
3.  `KnowledgeCompilation.execute(media_id, title, transcript)` -> `KnowledgeNode`

## 📊 Data Structures & Entities
The system uses `frozen=True` dataclasses for domain entities to ensure immutability and prevent side effects during state transitions.

### Key Entities:
-   `MediaSource`: id, url, status, title, audio_path.
-   `SpeechTranscript`: id, media_id, audio_path, text, status.
-   `KnowledgeNode`: id, media_id, title, content, tags, status.

---

## ⚙️ Configuration & Environment
-   **Framework**: `pydantic-settings` (V2).
-   **Fail-fast**: System fails during startup if required configurations are missing or invalid.
-   **Envs**: Managed via `.env` file with Pydantic validation.
