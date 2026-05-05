from abc import ABC, abstractmethod
from typing import List
from ias.modules.knowledge_compilation.domain.entities import KnowledgeNode

class KnowledgeSynthesizerPort(ABC):
    """
    Port (interface) for synthesizing raw text into structured knowledge using an LLM.
    """
    
    @abstractmethod
    async def synthesize(self, title: str, transcript: str) -> str:
        """
        Synthesizes the transcript into a Markdown structured content.
        """
        pass

class VaultRepositoryPort(ABC):
    """
    Port (interface) for persisting knowledge nodes into a vault (e.g., Obsidian).
    """
    
    @abstractmethod
    async def save(self, node: KnowledgeNode) -> None:
        """
        Saves the knowledge node to the vault.
        """
        pass
