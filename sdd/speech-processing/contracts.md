# Speech Processing, External Contracts

## OpenAI Whisper Interface

### Model Interaction
The system interacts with the Whisper model via the Python library wrapper.

| Parameter | Current Value | Rationale |
| :--- | :--- | :--- |
| **Model Size** | `base` (default) | Fast processing for average consumer CPUs. |
| **Input Format** | `mp3` | Compatible with `media_ingestion` output. |
| **Language Detection** | Automatic | Ensures support for multilingual sources. |

### Resource Consumption (Estimated)
- **VRAM/RAM**: ~500MB for `base`, up to ~10GB for `large-v3`.
- **CPU/GPU**: High utilization during the inference loop.

---

## Internal Data Contract

### Input: Audio File
- **Expectation**: Valid audio file accessible via local filesystem.
- **Source**: Typically provided by `media_ingestion`.

### Output: Transcript String
- **Format**: Plain text (UTF-8).
- **Structure**: Continuous string containing the full speech content.

---

## 🟢 Confidence: CONFIRMADO
Derived from `WhisperSpeechProcessor` implementation.
