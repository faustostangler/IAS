from dataclasses import dataclass
from typing import NewType
from enum import Enum

MediaId = NewType("MediaId", str)

class MediaStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass(frozen=True)
class MediaSource:
    """
    Domain entity representing a source of media (e.g., a YouTube URL).
    """
    id: MediaId
    url: str
    status: MediaStatus = MediaStatus.PENDING
    title: str = ""
    audio_path: str = ""

    def start_processing(self) -> "MediaSource":
        return MediaSource(
            id=self.id,
            url=self.url,
            status=MediaStatus.PROCESSING,
            title=self.title,
            audio_path=self.audio_path
        )

    def complete(self, title: str, audio_path: str) -> "MediaSource":
        return MediaSource(
            id=self.id,
            url=self.url,
            status=MediaStatus.COMPLETED,
            title=title,
            audio_path=audio_path
        )

    def fail(self) -> "MediaSource":
        return MediaSource(
            id=self.id,
            url=self.url,
            status=MediaStatus.FAILED,
            title=self.title,
            audio_path=self.audio_path
        )
