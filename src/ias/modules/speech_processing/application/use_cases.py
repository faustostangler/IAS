import uuid
from ias.modules.speech_processing.domain.entities import SpeechTranscript, TranscriptId
from ias.modules.speech_processing.domain.ports import SpeechProcessorPort

class TranscribeAudioUseCase:
    """
    Use case for transcribing an audio file.
    Coordinates the domain entities and the speech processing adapters.
    """
    
    def __init__(self, speech_processor: SpeechProcessorPort):
        self._speech_processor = speech_processor

    async def execute(self, media_id: str, audio_path: str) -> SpeechTranscript:
        # Create a new SpeechTranscript entity
        transcript_id = TranscriptId(str(uuid.uuid4()))
        transcript = SpeechTranscript(
            id=transcript_id,
            media_id=media_id,
            audio_path=audio_path
        )
        
        # Start processing
        transcript = transcript.start_processing()
        
        try:
            # Delegate transcription to the port
            updated_transcript = await self._speech_processor.transcribe(transcript)
            return updated_transcript
        except Exception:
            return transcript.fail()
