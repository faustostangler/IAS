from dataclasses import dataclass
from typing import NewType, List
from enum import Enum

NodeId = NewType("NodeId", str)

class CompilationStatus(Enum):
    PENDING = "pending"
    COMPILING = "compiling"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass(frozen=True)
class KnowledgeNode:
    """
    Domain entity representing a structured knowledge node (Markdown file).
    """
    id: NodeId
    media_id: str
    title: str
    content: str = ""
    tags: List[str] = None
    status: CompilationStatus = CompilationStatus.PENDING

    def start_compiling(self) -> "KnowledgeNode":
        return KnowledgeNode(
            id=self.id,
            media_id=self.media_id,
            title=self.title,
            status=CompilationStatus.COMPILING,
            tags=self.tags or []
        )

    def complete(self, content: str, tags: List[str] = None) -> "KnowledgeNode":
        return KnowledgeNode(
            id=self.id,
            media_id=self.media_id,
            title=self.title,
            content=content,
            tags=tags or self.tags or [],
            status=CompilationStatus.COMPLETED
        )

    def fail(self) -> "KnowledgeNode":
        return KnowledgeNode(
            id=self.id,
            media_id=self.media_id,
            title=self.title,
            status=CompilationStatus.FAILED,
            tags=self.tags or []
        )
