# Modules

In dependency order. A plan's prompt names modules by id.

| Id | Module | Depends on | Status |
|---|---|---|---|
| `work-email` | [Work email, and sign in with Google](work-email.md) | | Written |
| `password-manager` | [Password manager](password-manager.md) | `work-email` | Written |
| `hardware-keys` | [Hardware keys](hardware-keys.md) | `password-manager` | Written |
| `admin-split` | [Separate admin accounts](admin-split.md) | `hardware-keys` | Written |
| `admin-audit` | [Least-privilege admin audit](admin-audit.md) | `admin-split` | Written |
| `phone-sim` | [Phone and SIM hardening](phone-sim.md) | `admin-split` | Written |
| `ai-connector-scopes` | [AI connector scopes](ai-connector-scopes.md) | `password-manager` | Written |

Ids and check numbers are fixed from `v0.1` on.
