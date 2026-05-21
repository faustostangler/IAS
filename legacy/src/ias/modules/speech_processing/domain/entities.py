from dataclasses import dataclass
from typing import NewType
from enum import Enum

TranscriptId = NewType("TranscriptId", str)

class SpeechStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass(frozen=True)
class SpeechTranscript:
    """
    Domain entity representing a transcribed audio.
    """
    id: TranscriptId
    media_id: str
    audio_path: str
    text: str = ""
    status: SpeechStatus = SpeechStatus.PENDING

    def start_processing(self) -> "SpeechTranscript":
        return SpeechTranscript(
            id=self.id,
            media_id=self.media_id,
            audio_path=self.audio_path,
            status=SpeechStatus.PROCESSING
        )

    def complete(self, text: str) -> "SpeechTranscript":
        return SpeechTranscript(
            id=self.id,
            media_id=self.media_id,
            audio_path=self.audio_path,
            text=text,
            status=SpeechStatus.COMPLETED
        )

    def fail(self) -> "SpeechTranscript":
        return SpeechTranscript(
            id=self.id,
            media_id=self.media_id,
            audio_path=self.audio_path,
            status=SpeechStatus.FAILED
        )
