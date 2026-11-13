# Modules

In dependency order. A plan's prompt names modules by id.

| Id | Module | Depends on | Status |
|---|---|---|---|
| `work-email` | [Work email, and sign in with Google](work-email.md) | | Written |
| `password-manager` | [Password manager](password-manager.md) | `work-email` | Written |
| `hardware-keys` | Hardware keys | `password-manager` | Planned |
| `admin-split` | Super admin split | `hardware-keys` | Planned |
| `admin-audit` | Least-privilege admin audit | `admin-split` | Planned |
| `phone-sim` | Phone and SIM hardening | `password-manager` | Planned |
| `ai-connector-scopes` | AI connector scopes | `work-email` | Planned |

The planned ids and dependencies may still change until `v0.1` is
tagged. After that they are fixed.
