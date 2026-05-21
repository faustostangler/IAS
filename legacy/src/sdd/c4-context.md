# C4 Context Diagram — IAS

## 🌐 System Context
The Intelligent Audio Scriber (IAS) is a tool for developers and researchers to automate the process of turning video content into structured notes.

```mermaid
C4Context
    title System Context diagram for Intelligent Audio Scriber (IAS)

    Person(user, "User", "Researcher, Developer, or Content Consumer.")
    System(ias, "IAS System", "Automates media ingestion, transcription, and knowledge synthesis.")

    System_Ext(youtube, "YouTube", "External video platform (Source of media).")
    System_Ext(ollama, "Ollama", "Local LLM service for content synthesis.")
    System_Ext(whisper, "Local Whisper", "Local speech-to-text model (OpenAI).")
    System_Ext(obsidian, "Obsidian Vault", "Local Markdown-based knowledge base.")

    Rel(user, ias, "Provides URL, receives structured notes", "CLI / REST API")
    Rel(ias, youtube, "Extracts audio", "HTTPS / yt-dlp")
    Rel(ias, whisper, "Sends audio for transcription", "Local Execution")
    Rel(ias, ollama, "Sends transcript for synthesis", "HTTP / Port 11434")
    Rel(ias, obsidian, "Saves compiled knowledge (.md)", "Filesystem")
```

| Element | Type | Description |
| :--- | :--- | :--- |
| **User** | Person | Interacts with IAS to process URLs and organize knowledge. |
| **IAS System** | Software System | The core application orchestrating the transformation pipeline. |
| **YouTube** | External System | External media provider accessed via the ingestion module. |
| **Ollama** | External System | Local service providing LLM capabilities (Llama3, etc.). |
| **Local Whisper** | External System | Local library/model for processing audio into text. |
| **Obsidian Vault** | External System | The target knowledge storage for the synthesized notes. |
