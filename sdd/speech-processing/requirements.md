# Speech Processing

## Overview
Handles the transformation of audio content into textual transcripts using local AI models. It bridges the gap between raw audio signals and structured knowledge.

## Responsibilities
- Manage transcription requests for specific media sources. 🟢
- Interface with local OpenAI Whisper models. 🟢
- Handle long-running audio processing tasks asynchronously. 🟢
- Maintain transcription states (Pending, Processing, Completed, Failed). 🟢

## Business Rules
- **Prerequisite Check**: Transcription can only start if a valid `audio_path` is provided. 🟢
- **State Isolation**: Each transcription job is independent and identified by a `TranscriptId`. 🟢
- **Local Model usage**: Must use a locally hosted model as defined in system settings to ensure privacy. 🟢

## Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| RF-01 | Audio Transcription | Must | Given a valid audio path, the system generates a full text transcript. |
| RF-02 | Model Customization | Should | The system should allow selecting different Whisper model sizes (base, small, etc.) via config. |
| RF-03 | Async Execution | Must | Transcription must run without blocking the main application flow. |
| RF-04 | Checkpointing | Should | Skip transcription if a valid transcript already exists for the given media. |

## Non-Functional Requirements

| Type | Inferred Requirement | Evidence in Code | Confidence |
| :--- | :--- | :--- | :--- |
| Performance | Lazy Model Loading | `adapters.py:24` | 🟢 |
| Hardware | GPU Acceleration | `pyproject.toml:15` (torch dependency) | 🟢 |
| Reliability | Error State capture | `use_cases.py:31` | 🟢 |

## Acceptance Criteria

```gherkin
Scenario: Successful transcription
  Given a valid audio file at "/path/to/audio.mp3"
  When the TranscribeAudioUseCase is executed
  Then a SpeechTranscript is returned with status COMPLETED
  And the text field contains the transcribed speech

Scenario: Transcription failure (missing file)
  Given a non-existent audio path
  When the TranscribeAudioUseCase is executed
  Then a SpeechTranscript is returned with status FAILED
```

## Priority (Moscow)

| Requirement | MoSCoW | Rationale |
| :--- | :--- | :--- |
| Audio Transcription | Must | The core value proposition of the module. |
| Async Execution | Must | Essential for responsiveness given the high CPU/GPU cost of AI models. |
| Model Customization | Should | Important for different hardware capabilities but not for basic functionality. |

## Code Traceability

| File | Function / Class | Coverage |
| :--- | :--- | :--- |
| `src/ias/modules/speech_processing/domain/entities.py` | `SpeechTranscript`, `SpeechStatus` | 🟢 |
| `src/ias/modules/speech_processing/application/use_cases.py` | `TranscribeAudioUseCase` | 🟢 |
| `src/ias/modules/speech_processing/infrastructure/adapters.py` | `WhisperSpeechProcessor` | 🟢 |
