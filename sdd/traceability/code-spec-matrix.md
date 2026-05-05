# Code/Spec Matrix — IAS

This matrix maps legacy source files to their corresponding specification units and coverage confidence.

| Legacy File Path | Unit / Specification | Coverage | Confidence |
| :--- | :--- | :---: | :---: |
| `src/ias/modules/media_ingestion/domain/entities.py` | `media-ingestion` | Full | 🟢 |
| `src/ias/modules/media_ingestion/domain/ports.py` | `media-ingestion` | Full | 🟢 |
| `src/ias/modules/media_ingestion/application/use_cases.py` | `media-ingestion` | Full | 🟢 |
| `src/ias/modules/media_ingestion/infrastructure/adapters.py` | `media-ingestion` | Full | 🟢 |
| `src/ias/modules/speech_processing/domain/entities.py` | `speech-processing` | Full | 🟢 |
| `src/ias/modules/speech_processing/domain/ports.py` | `speech-processing` | Full | 🟢 |
| `src/ias/modules/speech_processing/application/use_cases.py` | `speech-processing` | Full | 🟢 |
| `src/ias/modules/speech_processing/infrastructure/adapters.py` | `speech-processing` | Full | 🟢 |
| `src/ias/modules/knowledge_compilation/domain/entities.py` | `knowledge-compilation` | Full | 🟢 |
| `src/ias/modules/knowledge_compilation/domain/ports.py` | `knowledge-compilation` | Full | 🟢 |
| `src/ias/modules/knowledge_compilation/application/use_cases.py` | `knowledge-compilation` | Full | 🟢 |
| `src/ias/modules/knowledge_compilation/infrastructure/adapters.py` | `knowledge-compilation` | Full | 🟢 |
| `src/ias/shared_kernel/orchestrator.py` | `shared-kernel` | Full | 🟢 |
| `src/ias/config.py` | `shared-kernel` | Full | 🟢 |
| `src/ias/main.py` | `shared-kernel` | Full | 🟢 |
| `src/ias/presentation/api.py` | `shared-kernel` / `openapi` | Full | 🟢 |

## 📊 Summary
- **Total Legacy Files**: 16
- **Mapped Files**: 16
- **Coverage**: 100%
- **Confidence**: 🟢 CONFIRMADO (Based on code analysis)

---

## 🟡 Inferências e Notas
- The mapping for `api.py` includes both the orchestration logic and the OpenAPI contract.
- All files in the `modules/` structure were successfully mapped to their respective Bounded Context units.
