# Media Ingestion, External Contracts

## YouTube Audio Extraction (yt-dlp)

### Interface Overview
The system integrates with YouTube via the `yt-dlp` library to extract high-quality audio.

### Technical Configuration
| Option | Value | Rationale |
| :--- | :--- | :--- |
| **Format** | `bestaudio/best` | Ensure highest possible quality before conversion. |
| **Codec** | `mp3` | Universal compatibility for transcription models. |
| **Bitrate** | `192 kbps` | Balance between quality and file size. |
| **Template** | `%(id)s.%(ext)s` | Use unique YouTube ID as filename to avoid collisions. |

### Data Structures (External)

#### yt-dlp Metadata Keys Used
- `id`: Unique video identifier (e.g., `aqz-KE-BPKQ`).
- `title`: Human-readable title of the video.
- `ext`: Original extension of the audio stream.

### Constraints and Limits
- **Network Dependency**: Requires stable internet access.
- **Process Blocking**: Extraction is synchronous; must be offloaded to a thread pool in async environments.
- **Rate Limiting**: Excessive requests might trigger YouTube's bot detection (no cookie support currently implemented).

---

## Storage Contract (Local Filesystem)

### Directory Structure
`{STORAGE_PATH}/audio/`

### File Naming Convention
`[media_id].mp3` (where `media_id` is the internal UUID v4). 🔴 [Decisão Fausto]

### Access Patterns
- **Write**: Sequential write during extraction.
- **Read**: Sequential read by the Speech Processing module.
- **Concurrency**: Multiple concurrent writes are safe as filenames are unique per video ID.

---

## 🟢 Confidence: CONFIRMADO
Extracted from `adapters.py` implementation of `YoutubeAudioExtractor`.
