# The module format

A module is one fix a small team can make itself. It is written for two
readers at once: the founder, who decides whether to spend the money and
the time, and the team's agent, which does the reading, the inventory and
the record-keeping while a person does anything that could lock someone
out.

Every module is one markdown file in [`modules/`](../modules/), named by
its id: `modules/<id>.md`. Copy [`module-template.md`](module-template.md)
to start one.

## Metadata

YAML front matter at the top of the file.

```yaml
---
id: password-manager          # stable; never renamed once tagged
title: Password manager
summary: One line for the index.
depends_on: [work-email]      # ids of modules to finish first
applies_to: [any]
default: 1Password Business   # the one vendor we name
fallback: Bitwarden Enterprise # only where a specific need calls for it, else omit
cost: $8.99 per person per month   # the short form; details in the body
time: 2 hours for the admin; 30-60 minutes per person
checked: 2026-11-12           # when the prices and vendor facts were last checked
---
```

- **`id`** is what a plan's prompt names. It never changes once a tag
  contains it. A module that needs a new id is a new module, and the old
  one says what replaced it.
- **`depends_on`** is the order. An agent does not start a module until
  every module it depends on is done or the plan says it was done another
  way.
- **`applies_to`** names the platforms the steps cover. The values in use:
  `google-workspace`, `microsoft-365`, `any`.
- **`cost`** is real money. A module that needs hardware or a paid tier
  says so here, and is never called free.
- **`checked`** is the date of the newest price or vendor fact in the
  module. Every price in the body carries its own date and source too.

## Sections, in this order

| Section | For | What goes in it |
|---|---|---|
| **The attack** | the founder | One sentence: what goes wrong without this fix. Real attacks, no scare words. |
| **Cost and time** | the founder | Money per person and in total, time for the admin and for each person, and anything it depends on (a key to buy, a paid tier). Dated. |
| **What done looks like** | both | Numbered checks anyone can verify: `D1`, `D2`, ... |
| **Steps** | both | Numbered steps, each with an owner (below), each pointing at the checks it satisfies. |
| **Agent instructions** | the agent | What to read and inventory first, what to propose, where to stop, what never to do. |
| **Evidence** | the checklist | For each check, what the agent records to show it's done. Never a secret. |
| **Variants** | both | Another platform, or the fallback vendor, and when to use it. Optional. |
| **Why this default** | the founder | Why we name this vendor and this setting, and what is given up. Short. |
| **Sources** | anyone | Vendor pages behind each price and fact, with the date checked. |

### Owners

Each step names who does it:

- **Agent**: reads, inventories, compares, drafts and records. It changes
  nothing that touches sign-in, admin rights, recovery or billing.
- **Agent, then a person confirms**: the agent proposes an exact change
  and a person says yes before it is made. Use this only for changes that
  can't lock anyone out, and only where the agent has been given access.
- **Person**: anything that can lock someone out, any purchase, anything
  that needs a person's own device, password or key. The agent explains
  the step, waits, then checks the result.
- **Person, each one**: a person's step that every person on the team
  does for their own account. The agent tracks who has done it.

When in doubt, a step belongs to a person.

### Checks

- Each check is something a stranger could verify by looking: a setting
  in a console, a report, a list. "Everyone understands" is not a check.
- Checks are numbered within the module (`D1`, `D2`, ...). The numbers
  are stable within a tag, so a checklist can say "work-email D3: done".
- A check may be marked **(later)** when a later module finishes it, for
  example when 2-Step Verification is turned on now and moved to hardware
  keys in `hardware-keys`. The later module names the check it finishes.

### Evidence

- Evidence is a fact about a setting, with a date and who checked it:
  "Admin console > Security > Authentication > 2-step verification: enforced for all
  users, 2026-11-12, checked by the agent from a screenshot the admin
  shared."
- **Never a secret.** No passwords, recovery codes, backup codes, keys,
  QR codes, tokens or full screenshots of a vault. If a check is about a
  secret, the evidence is where it is kept and who confirmed it, not the
  secret.
- Names of people and services in the team's own checklist are fine. The
  checklist lives with the team, never in this repo.

## Writing rules

- **Short sentences, plain words.** A founder with no security background
  should follow every line. Name the console path exactly (`Admin console
  > Security > Authentication > 2-Step Verification`) and check it against
  the vendor's current help pages.
- **One answer.** Name one default vendor and one setting. Add a fallback
  only for a specific need (the team must self-host, the team is already
  on another platform) and say what the need is.
- **Prices with dates.** Every price says when and where it was checked.
  Use list prices in US dollars, per person per month, annual billing,
  unless the module says otherwise.
- **Guidance only.** Modules tell the team how. They never say Bulkhead
  Labs, or anyone outside the team, will log in, buy, or administer.
- **Agent-agnostic.** Plain markdown. No syntax tied to one vendor's
  agent. Assume the agent can read files and web pages and may or may not
  have API access to the team's tools.
- **No client names, no call details.** Examples use invented teams.
