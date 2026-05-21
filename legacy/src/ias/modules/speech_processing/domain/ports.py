from abc import ABC, abstractmethod
from ias.modules.speech_processing.domain.entities import SpeechTranscript

class SpeechProcessorPort(ABC):
    """
    Port (interface) for transcribing audio to text.
    Following Hexagonal Architecture principles.
    """
    
    @abstractmethod
    async def transcribe(self, transcript: SpeechTranscript) -> SpeechTranscript:
        """
        Transcribes the audio file and returns an updated SpeechTranscript entity.
        """
        pass
