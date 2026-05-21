# Spec Impact Matrix — IAS

This matrix maps how changes in one module or component impact other parts of the system.

| Component / Module | Media Ingestion | Speech Processing | Knowledge Compilation | Shared Kernel | Presentation Layer |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Media Ingestion** | - | ⚡ High (Audio) | ⚡ Med (Metadata) | 🔗 Low | 🔗 Low |
| **Speech Processing** | ⚪ None | - | ⚡ High (Text) | 🔗 Low | 🔗 Low |
| **Knowledge Compilation** | ⚪ None | ⚪ None | - | 🔗 Low | 🔗 Low |
| **Shared Kernel** | ⚡ High (DI) | ⚡ High (DI) | ⚡ High (DI) | - | ⚡ High |
| **External: YouTube** | ⚡ High | ⚪ None | ⚪ None | ⚪ None | ⚪ None |
| **External: Whisper** | ⚪ None | ⚡ High | ⚪ None | ⚪ None | ⚪ None |
| **External: Ollama** | ⚪ None | ⚪ None | ⚡ High | ⚪ None | ⚪ None |

---

## ⚡ Legend
- **High Impact (⚡)**: Direct functional dependency. Changes in the source will likely break the target.
- **Medium Impact (⚡)**: Indirect dependency. Changes might require data format updates.
- **Low Impact (🔗)**: Common dependency (e.g., config, base classes).
- **None (⚪)**: No direct relationship.

## 📝 Critical Paths
1. **Audio Path Flow**: Media Ingestion extracts the audio file path used by Speech Processing. Any change in storage structure or naming convention in Ingestion directly impacts Speech.
2. **Media ID Flow**: The `media_id` is the primary key connecting all entities across Bounded Contexts.
3. **DI Injection**: The `Shared Kernel` / `main.py` is the composition root. Changes in adapter signatures impact the entire orchestration.
