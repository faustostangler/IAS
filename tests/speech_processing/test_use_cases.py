import pytest
from ias.modules.speech_processing.application.use_cases import TranscribeAudioUseCase
from ias.modules.speech_processing.domain.entities import SpeechTranscript, SpeechStatus
from ias.modules.speech_processing.domain.ports import SpeechProcessorPort

class MockSpeechProcessor(SpeechProcessorPort):
    async def transcribe(self, transcript: SpeechTranscript) -> SpeechTranscript:
        return transcript.complete(text="Hello world, this is a test transcription.")

@pytest.mark.asyncio
async def test_transcribe_audio_success():
    # Arrange
    processor = MockSpeechProcessor()
    use_case = TranscribeAudioUseCase(speech_processor=processor)
    media_id = "test-media-123"
    audio_path = "/tmp/test.mp3"
    
    # Act
    result = await use_case.execute(media_id, audio_path)
    
    # Assert
    assert result.status == SpeechStatus.COMPLETED
    assert result.text == "Hello world, this is a test transcription."
    assert result.media_id == media_id
    assert result.audio_path == audio_path
