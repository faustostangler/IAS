from abc import ABC, abstractmethod
from ias.modules.media_ingestion.domain.entities import MediaSource

class AudioExtractorPort(ABC):
    """
    Port (interface) for extracting audio from a media source.
    Following Hexagonal Architecture principles.
    """
    
    @abstractmethod
    async def extract_audio(self, source: MediaSource) -> MediaSource:
        """
        Extracts audio from the given source and returns an updated MediaSource entity.
        """
        pass
