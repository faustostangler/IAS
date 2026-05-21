# Ownership Map — IAS

This map cross-references the system modules with the contributors' commit activity to identify area experts and potential knowledge silos.

## Module Ownership
| Module | Main Contributor | Secondary Contributor | Knowledge Risk |
|--------|------------------|-----------------------|----------------|
| **media_ingestion** | Fausto Stangler | - | 🟢 Low (Single author, initial phase) |
| **speech_processing** | Fausto Stangler | - | 🟢 Low |
| **knowledge_compilation** | Fausto Stangler | - | 🟢 Low |
| **shared_kernel** | Fausto Stangler | - | 🟢 Low |
| **infrastructure (IaC)** | Fausto Stangler | - | 🟢 Low |

## Bus Factor Analysis
The project currently has a **Bus Factor of 1**. 

| Risk Level | Reason |
|------------|--------|
| **Operational** | Total dependency on Fausto Stangler for both business logic and architectural vision. |
| **Technical** | All automated documentation and code patterns were established by a single architect. |

## Knowledge Distribution Suggestions
1. **Peer Review**: As new developers join, prioritize reviews in the `shared-kernel` and `media-ingestion` modules, which are the most volatile and fundamental.
2. **Onboarding**: Use the existing SDDs in `sdd/` as the primary source for onboarding to mitigate the Bus Factor.
