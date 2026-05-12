import pytest
from ias.modules.knowledge_compilation.application.use_cases import CompileKnowledgeUseCase
from ias.modules.knowledge_compilation.domain.entities import KnowledgeNode, CompilationStatus
from ias.modules.knowledge_compilation.domain.ports import KnowledgeSynthesizerPort, VaultRepositoryPort

class MockSynthesizer(KnowledgeSynthesizerPort):
    async def synthesize(self, title: str, transcript: str) -> str:
        return f"# {title}\n\nProcessed content from transcript."

class MockVaultRepository(VaultRepositoryPort):
    def __init__(self):
        self.saved_nodes = []
    async def save(self, node: KnowledgeNode) -> None:
        self.saved_nodes.append(node)

@pytest.mark.asyncio
async def test_compile_knowledge_success():
    # Arrange
    synthesizer = MockSynthesizer()
    repository = MockVaultRepository()
    use_case = CompileKnowledgeUseCase(synthesizer=synthesizer, repository=repository)
    media_id = "test-media-123"
    title = "Test Video Title"
    transcript = "This is the raw transcript text."
    
    # Act
    result = await use_case.execute(media_id, title, transcript)
    
    # Assert
    assert result.status == CompilationStatus.COMPLETED
    assert "# Test Video Title" in result.content
    assert result.media_id == media_id
    assert len(repository.saved_nodes) == 1
    assert repository.saved_nodes[0].id == result.id
