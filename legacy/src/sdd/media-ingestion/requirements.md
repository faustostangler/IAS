# Media Ingestion

## Overview
Responsible for retrieving raw media content from external sources (URLs) and extracting high-quality audio streams for downstream processing. It acts as the gateway of the Intelligent Audio Scriber pipeline.

## Responsibilities
- Validate and ingest media URLs. 🟢
- Extract audio from video sources using external tools. 🟢
- Retrieve media metadata (e.g., title). 🟢
- Manage media processing states (Pending, Processing, Completed, Failed). 🟢

## Business Rules
- **Sequential Extraction**: Audio extraction must be triggered only after a `MediaSource` entity is initialized. 🟢
- **State Integrity**: A media source must move to `PROCESSING` state before extraction starts and `COMPLETED` only after successful save. 🟢
- **Fail-Fast**: Any extraction error must immediately move the entity to `FAILED` state to stop the pipeline. 🟢
- **Local Storage Preference**: Extracted audio must be stored in a locally configured storage path. 🟢
- **Checkpointing**: Before starting extraction, the system must check if the audio file already exists on disk to avoid redundant downloads. 🔴 [Decisão User]

## Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| RF-01 | Media Ingestion from URL | Must | Given a valid YouTube URL, the system creates a MediaSource entity. |
| RF-02 | Audio Extraction | Must | Given a MediaSource, the system extracts a 192kbps MP3 file to the storage path. |
| RF-03 | Metadata Retrieval | Should | The system should retrieve the video title and include it in the MediaSource entity. |
| RF-04 | State Management | Must | The entity status must accurately reflect the phase of the ingestion process. |

## Non-Functional Requirements

| Type | Inferred Requirement | Evidence in Code | Confidence |
| :--- | :--- | :--- | :--- |
| Performance | Non-blocking execution | `adapters.py:37` (uses `run_in_executor`) | 🟢 |
| Reliability | Exception handling | `use_cases.py:26` (try/except block) | 🟢 |
| Maintainability | Port/Adapter separation | `domain/ports.py` and `infrastructure/adapters.py` | 🟢 |

## Acceptance Criteria

```gherkin
Scenario: Successful audio extraction
  Given a valid YouTube URL "https://www.youtube.com/watch?v=..."
  When the IngestMediaUseCase is executed
  Then a MediaSource is returned with status COMPLETED
  And the audio_path points to a valid .mp3 file
  And the title is correctly populated

Scenario: Failed extraction on invalid URL
  Given an invalid URL "https://invalid.url"
  When the IngestMediaUseCase is executed
  Then a MediaSource is returned with status FAILED
```

## Priority (Moscow)

| Requirement | MoSCoW | Rationale |
| :--- | :--- | :--- |
| Audio Extraction | Must | Critical first step of the pipeline; without audio, transcription is impossible. |
| State Management | Must | Required for orchestrator control and error handling. |
| Title Retrieval | Should | Provides context for the user but doesn't block the functional pipeline. |

## Code Traceability

| File | Function / Class | Coverage |
| :--- | :--- | :--- |
| `src/ias/modules/media_ingestion/domain/entities.py` | `MediaSource`, `MediaStatus` | 🟢 |
| `src/ias/modules/media_ingestion/application/use_cases.py` | `IngestMediaUseCase` | 🟢 |
| `src/ias/modules/media_ingestion/infrastructure/adapters.py` | `YoutubeAudioExtractor` | 🟢 |
