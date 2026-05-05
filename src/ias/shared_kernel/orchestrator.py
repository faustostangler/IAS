from ias.modules.media_ingestion.application.use_cases import IngestMediaUseCase
from ias.modules.speech_processing.application.use_cases import TranscribeAudioUseCase
from ias.modules.knowledge_compilation.application.use_cases import CompileKnowledgeUseCase
from ias.modules.media_ingestion.domain.entities import MediaStatus
from ias.modules.speech_processing.domain.entities import SpeechStatus

class IASOrchestrator:
    """
    Orchestrates the entire pipeline across Bounded Contexts.
    Following the Modular Monolith pattern.
    """
    
    def __init__(
        self,
        ingest_use_case: IngestMediaUseCase,
        transcribe_use_case: TranscribeAudioUseCase,
        compile_use_case: CompileKnowledgeUseCase
    ):
        self._ingest = ingest_use_case
        self._transcribe = transcribe_use_case
        self._compile = compile_use_case

    async def process_url(self, url: str):
        """
        Runs the full pipeline: Ingest -> Transcribe -> Compile.
        """
        print(f"[*] Starting ingestion for: {url}")
        media = await self._ingest.execute(url)
        if media.status != MediaStatus.COMPLETED:
            print(f"[!] Ingestion failed for {url}")
            return
            
        print(f"[*] Transcription started for: {media.title}")
        transcript = await self._transcribe.execute(media.id, media.audio_path)
        if transcript.status != SpeechStatus.COMPLETED:
            print(f"[!] Transcription failed for {media.title}")
            return
            
        print(f"[*] Compilation started for: {media.title}")
        node = await self._compile.execute(media.id, media.title, transcript.text)
        
        print(f"[+] Knowledge compiled successfully: {node.title}")
        return node
