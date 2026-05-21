# Architecture Overview — IAS

## 🏗️ Architectural Pattern: Modular Monolith
The Intelligent Audio Scriber (IAS) is built as a **Modular Monolith**, ensuring a balance between logical separation of domains and operational simplicity. 

The system is organized into three core **Bounded Contexts**, each following the **Hexagonal Architecture (Ports & Adapters)** pattern to isolate domain logic from infrastructure concerns.

### Core Modules
1. **Media Ingestion**: Responsible for retrieving raw media content and extracting audio.
2. **Speech Processing**: Handles the conversion of audio speech into text transcripts.
3. **Knowledge Compilation**: Synthesizes transcripts into structured knowledge documents (Markdown).

---

## 🧩 Structural Components

### 1. Presentation Layer
- **CLI (`main.py`)**: Entry point for command-line interaction.
- **REST API (`api.py`)**: Entry point for web-based interaction (FastAPI).

### 2. Shared Kernel
- **Orchestrator**: Coordinates the workflow across different modules. It ensures the fail-fast sequential execution of the pipeline.
- **Config**: Centralized system settings using Pydantic.

### 3. Domain Core (Inside the Hexagon)
- Contains pure Business Logic, Entities, and Ports (Interfaces).
- Completely independent of external libraries like `yt-dlp`, `whisper`, or `ollama`.

### 4. Infrastructure Adapters (Outside the Hexagon)
- Concrete implementations of the domain ports.
- Swappable components for storage, AI processing, and media extraction.

---

## 📡 Communication Model
- **Internal**: Synchronous function calls between the Orchestrator and Module Use Cases.
- **Data Exchange**: Pass-by-value using immutable Domain Entities.
- **External**:
    - **YouTube**: HTTPS (via yt-dlp).
    - **Ollama**: Local HTTP API (port 11434).
    - **Filesystem**: Local I/O for audio and Markdown vault.

---

## 🟢 Scale of Confidence: CONFIRMADO
The architecture follows strict DDD and Clean Architecture principles as evidenced by the directory structure and implementation of Ports/Adapters.
