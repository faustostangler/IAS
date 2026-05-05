# Intelligent Audio Scriber

Intelligent Audio Scriber is a high-performance, local-first processing pipeline designed to transform unstructured multimedia content into structured, actionable domain knowledge. The system operates as a Clean Hexagonal Architecture-based Modular Monolith, integrating three distinct stages of execution: automated extraction of high-fidelity audio from video sources, local speech-to-text inference utilizing local Whisper, and semantic orchestration through a local LLM to generate strictly typed, structured data raw feed into Obsidian vault.

Built with a focus on privacy and data sovereignty, the project eliminates reliance on external cloud APIs by hosting the entire inference stack on-premises. Architecturally, it decouples the infrastructure adapters (YouTube scrapers and GPU-bound models) from the core application logic to ensure long-term maintainability and scalability.  

This tool is optimized for Generative AI patterns, fitting the event-driven triggers and dynamic task execution models used in modern AI agent orchestration. By converting raw audio into a "machine-readable blueprint," it enables advanced MD Knowledge Base and automated documentation for technical and research-oriented environments.

### Key Features

- **Local-First Architecture**: Runs entirely on-premises with no external API dependencies, ensuring data privacy and ownership.
- **Automated Video Processing**: Extracts high-fidelity audio from YouTube video sources, preparing it for analysis.
- **High-Accuracy Transcription**: Utilizes local Whisper models for fast and reliable speech-to-text conversion.
- **Structured Data Generation**: Transforms raw transcripts into semantically organized, structured, and machine-readable Markdown files using local LLMs.
- **Agentic Obsidian Maintanance**: The system automatically organizes the generated Markdown files into Obsidian vaults, creating a structured knowledge base, keeping it updated with new information.
- **Modular Design**: Clean Hexagonal Architecture ensures high maintainability and scalability.

