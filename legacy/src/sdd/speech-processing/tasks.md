# Speech Processing, Implementation Tasks

## Prerequisites
- [ ] Dependencies: `openai-whisper`, `torch`, `torchaudio`
- [ ] Pre-trained Whisper models accessible or downloadable

## Tasks

- [ ] T-01, Define Speech Processing Domain
  - Origin: `src/ias/modules/speech_processing/domain/entities.py`
  - Definition of Done: `SpeechTranscript` and `SpeechStatus` implemented.
  - Confidence: 🟢

- [ ] T-02, Define SpeechProcessorPort
  - Origin: `src/ias/modules/speech_processing/domain/ports.py`
  - Definition of Done: Interface defined for transcription capabilities.
  - Confidence: 🟢

- [ ] T-03, Implement TranscribeAudioUseCase
  - Origin: `src/ias/modules/speech_processing/application/use_cases.py`
  - Definition of Done: Workflow for entity state management and adapter call implemented.
  - Confidence: 🟢

- [ ] T-04, Implement WhisperSpeechProcessor Adapter
  - Origin: `src/ias/modules/speech_processing/infrastructure/adapters.py`
  - Definition of Done: Integration with `whisper` library, including lazy model loading.
  - Confidence: 🟢

## Test Tasks

- [ ] TT-01, Validate Full Transcription Cycle
  - Validates: `requirements.md` (Scenario: Successful transcription)
  - Method: Integration test with a 10-second sample audio file.

- [ ] TT-02, Validate OOM/Failure Handling
  - Validates: `requirements.md` (Scenario: Transcription failure)
  - Method: Mock the model to raise an exception and verify state moves to `FAILED`.

## Suggested Order
1. **Domain**: (T-01, T-02)
2. **Infrastructure**: (T-04) - Test model loading first.
3. **Application**: (T-03)

## Pending Gaps (🔴)
- **Progress Reporting**: No current mechanism to report % of completion for long audio files.
- **Concurrency Control**: Need to decide on a semaphore or queue to prevent multiple models from loading into VRAM simultaneously.
