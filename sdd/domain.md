# Domain Dictionary & Business Rules — IAS

## 📖 Glossary

| Term | Context | Definition |
| :--- | :--- | :--- |
| **MediaSource** | Media Ingestion | A domain entity representing a raw source of media (e.g., YouTube URL). |
| **MediaId** | Media Ingestion | A unique identifier (UUID v4) for a media source. |
| **Audio Extraction** | Media Ingestion | The process of pulling a high-quality audio stream from a media source. |
| **SpeechTranscript** | Speech Processing | A domain entity representing the textual representation of an audio file. |
| **TranscriptId** | Speech Processing | A unique identifier (UUID v4) for a transcript. |
| **Transcription** | Speech Processing | The process of converting speech from an audio file into text using an AI model. |
| **KnowledgeNode** | Knowledge Compilation | A domain entity representing structured knowledge extracted from a transcript. |
| **NodeId** | Knowledge Compilation | A unique identifier (UUID v4) for a knowledge node. |
| **Knowledge Compilation** | Knowledge Compilation | The process of synthesizing a transcript into structured Markdown/Obsidian format. |
| **Vault** | Knowledge Compilation | The destination storage for compiled knowledge (e.g., an Obsidian vault). |
| **Bounded Context** | Architecture | A logical boundary within the system where a specific domain model is valid. |

---

## 🛠️ Implicit Business Rules

### 1. Sequential Pipeline Execution
- **Rule**: The system must follow a strict sequential flow: Ingest -> Transcribe -> Compile.
- **Enforcement**: Orchestrated in `IASOrchestrator`. A failure in any stage prevents the next stage from starting (Fail-Fast).
- **Confidence**: 🟢 CONFIRMADO

### 2. Domain Entity Immutability
- **Rule**: Domain entities (MediaSource, SpeechTranscript, KnowledgeNode) must be immutable.
- **Enforcement**: Implemented using `frozen=True` in Python dataclasses. State changes return a new instance of the entity.
- **Confidence**: 🟢 CONFIRMADO

### 3. Local-First AI Processing
- **Rule**: AI processing (Speech-to-Text and Synthesis) should prefer local models (Whisper and Ollama/Llama3).
- **Enforcement**: Defined in `Settings` and implemented in default infrastructure adapters.
- **Confidence**: 🟢 CONFIRMADO

### 4. Persistence Agnosticism
- **Rule**: The domain core must not depend on specific persistence technologies.
- **Enforcement**: Use of Ports (Interfaces) for repositories and adapters for specific implementations (e.g., `ObsidianVaultRepository`).
- **Confidence**: 🟢 CONFIRMADO

### 5. Media Uniqueness
- **Rule**: Each processing request generates a new `MediaId` regardless of the URL.
- **Enforcement**: UUID v4 generation in use cases without URL-to-ID mapping (at current stage).
- **Confidence**: 🟡 INFERIDO (No database-level unique constraint on URL observed yet).
