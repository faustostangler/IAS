# Inventory - IAS

## 📁 Directory Structure
```
.
├── AGENTS.md
├── docker-compose.yml
├── Dockerfile
├── main.py (Link to src/ias/main.py)
├── Makefile
├── pyproject.toml
├── pytest.ini
├── README.md
├── src
│   ├── ias
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── modules
│   │   │   ├── knowledge_compilation
│   │   │   ├── media_ingestion
│   │   │   └── speech_processing
│   │   ├── presentation
│   │   │   └── api.py
│   │   └── shared_kernel
│   │       └── orchestrator.py
└── tests
    ├── knowledge_compilation
    ├── media_ingestion
    └── speech_processing
```

## 🛠️ Technologies & Frameworks
- **Primary Language**: Python (>= 3.13)
- **Frameworks**: FastAPI, SQLAlchemy, Pydantic V2
- **Tools**: uv (Package Manager), Ruff (Linter/Formatter), MyPy (Type Checker), Pytest (Testing)
- **AI/ML**: OpenAI Whisper (Local), Ollama (via API), yt-dlp (Audio Extraction)

## 🚀 Entry Points
- **API**: `src/ias/presentation/api.py` (FastAPI)
- **CLI**: `src/ias/main.py`
- **Orchestrator**: `src/ias/shared_kernel/orchestrator.py`

## 🏗️ Infrastructure
- **Docker**: `Dockerfile` (Multi-stage, uv-based), `docker-compose.yml`
- **Automation**: `Makefile` (up, down, logs, test, lint, format)

## 🧪 Testing
- **Framework**: Pytest
- **Coverage Estimation**: 3 test files (100% of modules covered with use case tests)
- **Plugins**: pytest-asyncio
