import asyncio
import whisper
from ias.modules.speech_processing.domain.entities import SpeechTranscript
from ias.modules.speech_processing.domain.ports import SpeechProcessorPort
from ias.config import settings

class WhisperSpeechProcessor(SpeechProcessorPort):
    """
    Adapter for transcribing audio using local OpenAI Whisper.
    Implements the SpeechProcessorPort.
    """
    
    def __init__(self, model_name: str = None):
        self.model_name = model_name or settings.WHISPER_MODEL
        self._model = None

    async def transcribe(self, transcript: SpeechTranscript) -> SpeechTranscript:
        """
        Transcribes the audio file using Whisper.
        """
        try:
            # Load model lazily
            if self._model is None:
                self._model = whisper.load_model(self.model_name)
            
            # Run transcription in a separate thread
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(None, lambda: self._model.transcribe(transcript.audio_path))
            
            text = result.get('text', '').strip()
            return transcript.complete(text=text)
        except Exception:
            return transcript.fail()
