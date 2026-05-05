import uuid
from ias.modules.knowledge_compilation.domain.entities import KnowledgeNode, NodeId, CompilationStatus
from ias.modules.knowledge_compilation.domain.ports import KnowledgeSynthesizerPort, VaultRepositoryPort

class CompileKnowledgeUseCase:
    """
    Use case for synthesizing a transcript into a structured knowledge node and saving it to a vault.
    Coordinates the domain entities and the infrastructure adapters.
    """
    
    def __init__(self, synthesizer: KnowledgeSynthesizerPort, repository: VaultRepositoryPort):
        self._synthesizer = synthesizer
        self._repository = repository

    async def execute(self, media_id: str, title: str, transcript_text: str) -> KnowledgeNode:
        # Create a new KnowledgeNode entity
        node_id = NodeId(str(uuid.uuid4()))
        node = KnowledgeNode(
            id=node_id,
            media_id=media_id,
            title=title
        )
        
        # Start compiling
        node = node.start_compiling()
        
        try:
            # Delegate synthesis to the port
            content = await self._synthesizer.synthesize(title, transcript_text)
            
            # Update the node with synthesized content
            node = node.complete(content=content)
            
            # Persist the node into the vault
            await self._repository.save(node)
            
            return node
        except Exception:
            return node.fail()
