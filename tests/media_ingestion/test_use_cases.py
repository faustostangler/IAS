import pytest
from unittest.mock import AsyncMock
from ias.modules.media_ingestion.application.use_cases import IngestMediaUseCase
from ias.modules.media_ingestion.domain.entities import MediaSource, MediaStatus, MediaId
from ias.modules.media_ingestion.domain.ports import AudioExtractorPort

class MockAudioExtractor(AudioExtractorPort):
    async def extract_audio(self, source: MediaSource) -> MediaSource:
        return source.complete(title="Test Video", audio_path="/tmp/test.mp3")

@pytest.mark.asyncio
async def test_ingest_media_success():
    # Arrange
    extractor = MockAudioExtractor()
    use_case = IngestMediaUseCase(audio_extractor=extractor)
    url = "https://www.youtube.com/watch?v=fOR6Kpthk2E"
    
    # Act
    result = await use_case.execute(url)
    
    # Assert
    assert result.status == MediaStatus.COMPLETED
    assert result.title == "Test Video"
    assert result.audio_path == "/tmp/test.mp3"
    assert result.url == url
