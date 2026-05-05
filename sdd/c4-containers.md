# C4 Containers Diagram — IAS

## 📦 Container Vision
The IAS system is designed as a Modular Monolith, where all modules run within the same process but are logically isolated.

```mermaid
C4Container
    title Container diagram for Intelligent Audio Scriber (IAS)

    Person(user, "User", "Researcher or Developer")

    Container_Boundary(ias_app, "IAS Application (Python Monolith)") {
        Component(api, "FastAPI / CLI", "Python/FastAPI", "Entry point for users and external clients.")
        Component(orchestrator, "IAS Orchestrator", "Python", "Coordinates cross-module workflows.")
        
        Container_Boundary(modules, "Bounded Contexts") {
            Component(ingestion, "Media Ingestion", "Hexagonal Module", "Handles URL ingestion and audio extraction.")
            Component(speech, "Speech Processing", "Hexagonal Module", "Handles transcription logic.")
            Component(compilation, "Knowledge Compilation", "Hexagonal Module", "Handles synthesis and vault storage.")
        }
    }

    ContainerDb(data_store, "Local Storage", "Filesystem", "Stores temporary audio files and system metadata.")
    Container(ollama_svc, "Ollama Service", "Container/Binary", "Provides LLM via Local HTTP API.")
    Container(obsidian_vault, "Obsidian Vault", "Folder", "Target destination for Markdown files.")

    Rel(user, api, "Uses", "HTTPS/CLI")
    Rel(api, orchestrator, "Calls")
    Rel(orchestrator, ingestion, "Triggers Ingestion")
    Rel(orchestrator, speech, "Triggers Transcription")
    Rel(orchestrator, compilation, "Triggers Compilation")

    Rel(ingestion, data_store, "Saves audio", "File I/O")
    Rel(speech, data_store, "Reads audio", "File I/O")
    Rel(compilation, ollama_svc, "Sends transcript", "HTTP/11434")
    Rel(compilation, obsidian_vault, "Saves .md notes", "File I/O")
```

| Container | Technology | Description |
| :--- | :--- | :--- |
| **IAS Application** | Python | The main application process containing all logic and modules. |
| **Local Storage** | Filesystem | Persistent storage for processed audio and local cache. |
| **Ollama Service** | Ollama | External local service for AI synthesis. |
| **Obsidian Vault** | Filesystem | The user's personal knowledge base folder. |
