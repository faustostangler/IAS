# Intelligent Audio Scriber (IAS)

Intelligent Audio Scriber is a high-performance, local-first processing pipeline designed to transform unstructured multimedia content into structured, actionable domain knowledge. The system operates as a **Modular Monolith** built on **Clean Hexagonal Architecture**, ensuring that core domain logic remains decoupled from infrastructure dependencies such as extraction tools and AI models.

Built with a focus on privacy and data sovereignty, IAS eliminates reliance on external cloud APIs by hosting the entire inference stack on-premises. This architecture is optimized for modern AI agent orchestration, converting raw audio into "machine-readable blueprints" for advanced Obsidian Knowledge Bases.

---

## 🚀 Key Features

- **Local-First AI**: Zero external API dependencies. Runs `Whisper` and `Ollama` locally.
- **Automated Ingestion**: Seamless audio extraction from YouTube sources via `yt-dlp`.
- **High-Fidelity Transcription**: Leverages OpenAI's Whisper (base model) for robust speech-to-text.
- **Semantic Synthesis**: Transforms raw transcripts into structured Markdown nodes using local LLMs (e.g., Llama 3).
- **Vault Automation**: Managed persistence directly into Obsidian vaults with YAML frontmatter.
- **Fail-Fast Pipeline**: Strict sequential orchestration ensuring process integrity and resource efficiency.

---

## 🏗️ Technical Architecture

The system follows a **Modular Monolith** pattern with strict Bounded Contexts:

### 1. Media Ingestion
- **Port**: `AudioExtractorPort`
- **Adapter**: `YoutubeAudioExtractor` (wraps `yt-dlp`)
- **Strategy**: Extracts high-quality 192kbps MP3 audio. Uses internal UUID v4 for domain identity, isolating the system from external URL volatility.

### 2. Speech Processing
- **Port**: `SpeechProcessorPort`
- **Adapter**: `WhisperSpeechProcessor` (wraps `openai-whisper`)
- **Strategy**: Lazy-loads models into VRAM/RAM only when needed. Offloads CPU/GPU intensive tasks to background executors.

### 3. Knowledge Compilation
- **Port**: `KnowledgeSynthesizerPort`, `VaultRepositoryPort`
- **Adapter**: `OllamaSynthesizer`, `ObsidianVaultRepository`
- **Strategy**: Implements text chunking/Map-Reduce for long transcripts. Standardizes output into Markdown with YAML metadata.

---

## 🛠️ Technology Stack

- **Runtime**: Python 3.13+
- **Dependency Management**: [uv](https://github.com/astral-sh/uv) (Blazing fast Rust-based manager)
- **Web Framework**: FastAPI (Asynchronous API gateway)
- **AI/ML**: `torch`, `openai-whisper`, `yt-dlp`
- **LLM Engine**: [Ollama](https://ollama.com/) (Local HTTP API)
- **Validation**: Pydantic V2 (Settings & Entity validation)

---

## 🚦 Getting Started

### Prerequisites
1. Install **uv**: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Install **Ollama** and pull your model: `ollama pull llama3`

### Installation
```bash
# Clone the repository
git clone <repo-url>
cd IAS

# Install dependencies and create virtual environment
uv sync
```

### Execution
You can trigger the pipeline via CLI:
```bash
uv run ias "https://www.youtube.com/watch?v=..."
```

Or run the API server:
```bash
uv run uvicorn ias.presentation.api:app --reload
```

---

## 📝 Technical Specifications (SDD)

This project has been fully reverse-engineered and documented using the **Reversa** framework. Detailed technical specifications, including C4 diagrams, ERDs, and implementation tasks, can be found in the [sdd/](sdd/) directory:

- [Architecture Overview](sdd/architecture.md)
- [Domain & Business Rules](sdd/domain.md)
- [C4 Component Diagram](sdd/c4-components.md)
- [Traceability Matrix](sdd/traceability/code-spec-matrix.md)

---

## ⚖️ Architectural Decisions (ADRs)

1. **Internal Identity**: All domain entities use UUID v4. External IDs (like YouTube tags) are treated as secondary metadata.
2. **Sequential Queue**: To protect hardware resources (VRAM), the system processes only one request at a time.
3. **Local-First Sovereignty**: No data ever leaves the local environment, ensuring maximum privacy and zero latency from cloud providers.
