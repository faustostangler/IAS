import asyncio
import os
from yt_dlp import YoutubeDL
from ias.modules.media_ingestion.domain.entities import MediaSource
from ias.modules.media_ingestion.domain.ports import AudioExtractorPort
from ias.config import settings

class YoutubeAudioExtractor(AudioExtractorPort):
    """
    Adapter for extracting audio from YouTube using yt-dlp.
    Implements the AudioExtractorPort.
    """
    
    def __init__(self, output_dir: str = None):
        self.output_dir = output_dir or os.path.join(settings.STORAGE_PATH, "audio")
        os.makedirs(self.output_dir, exist_ok=True)

    async def extract_audio(self, source: MediaSource) -> MediaSource:
        """
        Downloads audio from YouTube and returns the updated MediaSource.
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{self.output_dir}/%(id)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            # Run yt-dlp in a separate thread to avoid blocking the event loop
            loop = asyncio.get_running_loop()
            info = await loop.run_in_executor(None, lambda: self._download(ydl_opts, source.url))
            
            title = info.get('title', 'Unknown Title')
            audio_path = f"{self.output_dir}/{info['id']}.mp3"
            
            return source.complete(title=title, audio_path=audio_path)
        except Exception as e:
            # In a real app, we would log the error "why" here
            return source.fail()

    def _download(self, opts: dict, url: str) -> dict:
        with YoutubeDL(opts) as ydl:
            return ydl.extract_info(url, download=True)
