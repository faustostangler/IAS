import asyncio
import sys
from ias.shared_kernel.orchestrator import IASOrchestrator
from ias.modules.media_ingestion.application.use_cases import IngestMediaUseCase
from ias.modules.media_ingestion.infrastructure.adapters import YoutubeAudioExtractor
from ias.modules.speech_processing.application.use_cases import TranscribeAudioUseCase
from ias.modules.speech_processing.infrastructure.adapters import WhisperSpeechProcessor
from ias.modules.knowledge_compilation.application.use_cases import CompileKnowledgeUseCase
from ias.modules.knowledge_compilation.infrastructure.adapters import OllamaSynthesizer, ObsidianVaultRepository

async def main():
    # Dependency Injection (Manual for simplicity in this Monolith)
    ingest_adapter = YoutubeAudioExtractor()
    speech_adapter = WhisperSpeechProcessor()
    compile_synthesizer = OllamaSynthesizer()
    compile_repo = ObsidianVaultRepository()
    
    orchestrator = IASOrchestrator(
        ingest_use_case=IngestMediaUseCase(ingest_adapter),
        transcribe_use_case=TranscribeAudioUseCase(speech_adapter),
        compile_use_case=CompileKnowledgeUseCase(compile_synthesizer, compile_repo)
    )
    
    if len(sys.argv) < 2:
        print("Usage: python -m ias.main <youtube_url>")
        return
        
    url = sys.argv[1]
    await orchestrator.process_url(url)

if __name__ == "__main__":
    asyncio.run(main())
