import os
import aiofiles
from ias.modules.knowledge_compilation.domain.entities import KnowledgeNode
from ias.modules.knowledge_compilation.domain.ports import VaultRepositoryPort, KnowledgeSynthesizerPort
from ias.config import settings

class ObsidianVaultRepository(VaultRepositoryPort):
    """
    Adapter for saving knowledge nodes as Markdown files in an Obsidian vault.
    Implements the VaultRepositoryPort.
    """
    
    def __init__(self, vault_path: str = None):
        self.vault_path = vault_path or settings.OBSIDIAN_VAULT_PATH or os.path.join(settings.STORAGE_PATH, "vault")
        os.makedirs(self.vault_path, exist_ok=True)

    async def save(self, node: KnowledgeNode) -> None:
        """
        Saves the node content to a .md file in the vault.
        """
        filename = f"{node.title.replace('/', '-')}.md"
        file_path = os.path.join(self.vault_path, filename)
        
        content_with_metadata = self._format_content(node)
        
        async with aiofiles.open(file_path, mode='w', encoding='utf-8') as f:
            await f.write(content_with_metadata)

    def _format_content(self, node: KnowledgeNode) -> str:
        tags_str = "\n".join([f"- {tag}" for tag in (node.tags or [])])
        metadata = f"---\nmedia_id: {node.media_id}\ntags:\n{tags_str}\n---\n\n"
        return metadata + node.content

class OllamaSynthesizer(KnowledgeSynthesizerPort):
    """
    Adapter for synthesizing knowledge using a local Ollama instance.
    Implements the KnowledgeSynthesizerPort.
    """
    
    def __init__(self, model_name: str = None):
        self.model_name = model_name or settings.LLM_MODEL
        self.api_url = "http://localhost:11434/api/generate"

    async def synthesize(self, title: str, transcript: str) -> str:
        """
        Calls local Ollama API to synthesize the transcript.
        """
        import httpx
        
        prompt = f"""
        You are an expert knowledge architect. Synthesize the following transcript into a structured, high-quality Markdown document.
        Use headers, bullet points, and highlight key concepts.
        
        Title: {title}
        Transcript:
        {transcript}
        """
        
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                self.api_url,
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json().get('response', '')
