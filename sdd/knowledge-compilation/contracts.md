# Knowledge Compilation, External Contracts

## Ollama API Interface

### API Specification
- **Endpoint**: `POST http://localhost:11434/api/generate`
- **Format**: JSON

### Request Payload
| Field | Type | Description |
| :--- | :--- | :--- |
| `model` | string | LLM model name (e.g., `llama3`). |
| `prompt` | string | Full synthesis prompt including title and transcript. |
| `stream` | boolean | Set to `false` for simplified single response. |

### Response Schema
```json
{
  "model": "llama3",
  "created_at": "...",
  "response": "Synthesized text content...",
  "done": true
}
```

---

## Vault Persistence Contract (Obsidian)

### File Format
- **Extension**: `.md`
- **Encoding**: `UTF-8`

### Document Structure (Template)
```markdown
---
media_id: [UUID]
tags:
- tag1
- tag2
---

[Synthesized Content from LLM]
```

### Directory Requirements
- Root path defined by `OBSIDIAN_VAULT_PATH` or `STORAGE_PATH/vault`.
- Subdirectories must be created if they don't exist.

---

## 🟢 Confidence: CONFIRMADO
Derived from `OllamaSynthesizer` and `ObsidianVaultRepository` adapters.
