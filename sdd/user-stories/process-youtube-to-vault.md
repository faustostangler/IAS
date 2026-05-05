# User Story: Process YouTube to Vault

## Description
As a researcher, I want to provide a YouTube URL and receive a structured Markdown note in my Obsidian vault, so that I can quickly reference and organize knowledge from video content without manual transcription.

## Persona
- **User**, a developer/researcher who uses Obsidian for personal knowledge management.

## Flow: "The Knowledge Pipeline"

### 1. Ingestion
- **Action**: User submits a URL via CLI or API.
- **System**:
    - Validates the URL.
    - Downloads audio using `yt-dlp`.
    - Stores the .mp3 file in the local data directory.
    - Captures the video title.

### 2. Transcription
- **System**:
    - Detects the presence of the new audio file.
    - Loads the local Whisper model (base).
    - Processes the audio and generates a plain text transcript.
    - Updates the processing state.

### 3. Synthesis
- **System**:
    - Sends the raw transcript and title to the local Ollama instance.
    - Prompts the LLM to structure the content into headers and bullet points.
    - Receives the synthesized Markdown content.

### 4. Persistence
- **System**:
    - Formats the content with YAML frontmatter (ID, tags).
    - Saves the file as `[Title].md` in the configured Obsidian Vault.
    - Notifies completion.

## Business Value
- **Time Saving**: Automates ~20-60 minutes of manual work per hour of video.
- **Privacy**: No audio or text leaves the local machine (using local Whisper and local LLM).
- **Searchability**: Content becomes searchable within Obsidian immediately.

## Success Criteria
- [ ] Audio file extracted successfully.
- [ ] Transcript accurately reflects video content.
- [ ] Markdown file exists in the vault with correct formatting.
