import uuid
from ias.modules.media_ingestion.domain.entities import MediaSource, MediaId, MediaStatus
from ias.modules.media_ingestion.domain.ports import AudioExtractorPort

class IngestMediaUseCase:
    """
    Use case for ingesting a media source from a URL.
    Coordinates the domain entities and the infrastructure adapters.
    """
    
    def __init__(self, audio_extractor: AudioExtractorPort):
        self._audio_extractor = audio_extractor

    async def execute(self, url: str) -> MediaSource:
        # Create a new MediaSource entity in PENDING state
        media_id = MediaId(str(uuid.uuid4()))
        source = MediaSource(id=media_id, url=url)
        
        # Start processing
        source = source.start_processing()
        
        try:
            # Delegate audio extraction to the port
            updated_source = await self._audio_extractor.extract_audio(source)
            return updated_source
        except Exception:
            return source.fail()
