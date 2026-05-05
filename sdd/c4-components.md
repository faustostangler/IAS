# C4 Components Diagram — IAS (Module Level)

## 🧩 Internal Component Structure
Each Bounded Context (Module) in IAS follows the same internal architectural pattern.

```mermaid
C4Component
    title Component diagram for an IAS Module (Hexagonal)

    Container(orchestrator, "IAS Orchestrator", "Python", "Calls the application layer.")

    Container_Boundary(module_boundary, "Bounded Context (e.g., Media Ingestion)") {
        Component(use_case, "Use Case", "Application Service", "Implements business workflow and orchestrates domain.")
        Component(entity, "Domain Entity", "Dataclass", "Core domain state and rules (Immutable).")
        Component(port, "Domain Port", "Abstract Class/Interface", "Definition of required infrastructure capability.")
        
        Container_Boundary(infra_boundary, "Infrastructure") {
            Component(adapter, "Adapter", "Concrete Implementation", "Implements the Port using external libraries (e.g., yt-dlp).")
        }
    }

    System_Ext(external, "External Technology", "Library or Service")

    Rel(orchestrator, use_case, "Executes", "async function call")
    Rel(use_case, entity, "Manages/Creates")
    Rel(use_case, port, "Uses")
    Rel(adapter, port, "Implements")
    Rel(adapter, external, "Interacts with", "API/Library calls")
```

### Components Responsibilities

| Component | Responsibility | Independence |
| :--- | :--- | :--- |
| **Use Case** | Orchestrates domain entities and ports to satisfy a user story. | Independent of Infra. |
| **Domain Entity** | Represents a business concept and its state transitions. | Highest Independence. |
| **Domain Port** | Defines the contract for external communication (SPI). | Part of the Domain. |
| **Adapter** | Translates the domain contract into technical implementation. | Low Independence (coupled to tech). |

---

## 🟢 Confidence: CONFIRMADO
The project strictly implements these layers in `application/`, `domain/`, and `infrastructure/` subdirectories for every module.
