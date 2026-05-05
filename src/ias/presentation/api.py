from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from ias.shared_kernel.orchestrator import IASOrchestrator
from ias.modules.media_ingestion.application.use_cases import IngestMediaUseCase
from ias.modules.media_ingestion.infrastructure.adapters import YoutubeAudioExtractor
from ias.modules.speech_processing.application.use_cases import TranscribeAudioUseCase
from ias.modules.speech_processing.infrastructure.adapters import WhisperSpeechProcessor
from ias.modules.knowledge_compilation.application.use_cases import CompileKnowledgeUseCase
from ias.modules.knowledge_compilation.infrastructure.adapters import OllamaSynthesizer, ObsidianVaultRepository

app = FastAPI(title="Intelligent Audio Scriber API")

# Dependency Injection
orchestrator = IASOrchestrator(
    ingest_use_case=IngestMediaUseCase(YoutubeAudioExtractor()),
    transcribe_use_case=TranscribeAudioUseCase(WhisperSpeechProcessor()),
    compile_use_case=CompileKnowledgeUseCase(OllamaSynthesizer(), ObsidianVaultRepository())
)

class ProcessRequest(BaseModel):
    url: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/process")
async def process(request: ProcessRequest, background_tasks: BackgroundTasks):
    """
    Triggers the full IAS pipeline for a given URL in the background.
    """
    background_tasks.add_task(orchestrator.process_url, request.url)
    return {"message": "Processing started", "url": request.url}
