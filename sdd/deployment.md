# Deployment Diagram — IAS

## 🚀 Infrastructure Vision
The system is designed to run in a containerized environment, ensuring all AI dependencies (Torch, Whisper) are pre-configured.

```mermaid
deploymentDiagram
    node UserMachine [
        User Machine
        (Ubuntu/Linux)
    ]

    node DockerHost [
        Docker Container Host
    ] {
        node IASContainer [
            IAS Container
            (Python 3.13 / Debian Slim)
        ] {
            artifact IASApp [
                IAS Application
            ]
        }
        
        node OllamaContainer [
            Ollama Container
            (Optional)
        ] {
            artifact Llama3 [
                Llama 3 Model
            ]
        }
    }

    node ExternalSystems [
        External Cloud / Internet
    ] {
        node YouTube [
            YouTube API
        ]
    }

    UserMachine -- DockerHost : "Runs docker-compose"
    IASContainer -- YouTube : "Extracts Audio (HTTPS)"
    IASContainer -- OllamaContainer : "Synthesizes Content (HTTP/11434)"
    IASContainer -- UserMachine : "Mounts /data and /vault (Volumes)"
```

## 🛠️ Deployment Configuration

### 1. Dockerfile Analysis
- **Base Image**: `python:3.13-slim` (Confirmed in `surface.json`).
- **Optimization**: Uses `uv` for fast dependency installation.
- **Hardware Access**: Requires volume mounting for persistent data.

### 2. Docker Compose Strategy
- **Single Service**: The Monolith runs as a single service.
- **Persistence**: Maps local host directories to `/app/data` for audio and `/app/vault` for notes.
- **Network**: Uses standard bridge network to communicate with local Ollama instance (typically on host).

---

## 🏗️ Technical Debt & Recommendations
1. **GPU Support**: The current Dockerfile might not include NVIDIA/CUDA drivers for GPU acceleration of Whisper/Torch.
2. **Healthchecks**: No healthchecks defined in docker-compose for the main application.
3. **Model Caching**: Whisper models are downloaded at runtime (or first use). Recommendation: Cache models in a volume to avoid redundant downloads.
