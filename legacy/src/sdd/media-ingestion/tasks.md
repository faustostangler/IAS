# Media Ingestion, Implementation Tasks

## Prerequisites
- [ ] Dependencies: `yt-dlp`, `asyncio`, `uuid`
- [ ] Base storage path configured in `Settings`

## Tasks

- [ ] T-01, Define Domain Entities and Status Enum
  - Origin: `src/ias/modules/media_ingestion/domain/entities.py`
  - Definition of Done: `MediaSource` and `MediaStatus` are implemented with immutability.
  - Confidence: 🟢

- [ ] T-02, Define AudioExtractorPort Interface
  - Origin: `src/ias/modules/media_ingestion/domain/ports.py`
  - Definition of Done: Abstract base class `AudioExtractorPort` defines `extract_audio` method.
  - Confidence: 🟢

- [ ] T-03, Implement IngestMediaUseCase
  - Origin: `src/ias/modules/media_ingestion/application/use_cases.py`
  - Definition of Done: Use case orchestrates entity creation, state changes, and calls the port.
  - Confidence: 🟢

- [ ] T-04, Implement YoutubeAudioExtractor Adapter
  - Origin: `src/ias/modules/media_ingestion/infrastructure/adapters.py`
  - Definition of Done: Adapter correctly wraps `yt-dlp`, uses `run_in_executor`, and saves .mp3 files.
  - Confidence: 🟢

## Test Tasks

- [ ] TT-01, Verify Successful Ingestion Workflow
  - Validates: `requirements.md` (Scenario: Successful audio extraction)
  - Method: Integration test with a known valid URL (e.g., a small public domain video).

- [ ] TT-02, Verify Error Handling for Invalid URLs
  - Validates: `requirements.md` (Scenario: Failed extraction on invalid URL)
  - Method: Mock `YoutubeDL` to throw an exception and verify status is `FAILED`.

## Suggested Order
1. **Domain First**: T-01 and T-02 provide the contract.
2. **Infrastructure Second**: T-04 allows testing the extraction logic independently.
3. **Application Last**: T-03 ties everything together.

## Pending Gaps (🔴)
- **URL Validation**: Need to decide if URL validation should happen at the Use Case level or inside the Adapter.
- **Cleanup Policy**: No task currently handles cleaning up partial downloads on failure.
