# Permissions & Access Control (RBAC/ACL) — IAS

## 🛡️ Current Access Model
As of the current version, the Intelligent Audio Scriber (IAS) operates as a **single-user system** (Local-First/CLI/Playground). There is no formal authentication or authorization layer implemented in the domain or application layers.

| Role | Access Level | Description |
| :--- | :--- | :--- |
| **System Operator** | Full Access | The user running the script or API has full access to all modules and local storage. |

---

## 🚫 Missing Controls (Security Gap Analysis)
Based on the architecture analysis, the following controls are currently absent:

1. **Multi-tenancy**: All data is stored in a shared `./data` directory. There is no isolation between different users or "owners" of the media sources.
2. **API Protection**: The presentation layer (FastAPI) does not include middleware for JWT or API Key validation.
3. **Vault Isolation**: If multiple Obsidian vaults are used, the system only supports one active vault defined in the global settings.

---

## 🟢 Confidence: CONFIRMADO
- No `auth` or `identity` modules found in `src/ias/modules`.
- No security dependencies (e.g., `python-jose`, `passlib`) found in `pyproject.toml`.
- `Settings` class does not contain authentication parameters.
