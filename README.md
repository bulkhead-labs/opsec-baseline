<p>
  <a href="https://bulkheadlabs.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/bulkhead-lockup-dark.svg">
      <img src="assets/bulkhead-lockup-light.svg" alt="Bulkhead Labs" width="200">
    </picture>
  </a>
</p>

# OPSEC baseline

**The security basics a small team can do itself, written so the team's
own agent can help.** Each module is one fix: what goes wrong without it,
what it costs, what done looks like, and steps split between the team's
people and its agent. The agent reads, inventories and keeps the
checklist. A person does anything that could lock someone out.

**New here? Read [Seven Walls](https://bulkhead-labs.github.io/opsec-baseline/)**,
the story of one small company's year and the seven walls that held. No
technical background needed.

> **Status: v0.1 in progress.** Two of the first seven modules are
> written. Until `v0.1` is tagged there is nothing to pin. Follow the
> [v0.1 milestone](https://github.com/bulkhead-labs/opsec-baseline/milestone/1).

## The modules

Roughly in dependency order. Each module names the ones it needs first.

| | Module | Fixes | You pay for |
|---|---|---|---|
| 1 | [Work email, and sign in with Google](modules/work-email.md) | Personal accounts, a password per tool, nowhere to shut the door when someone leaves | A Workspace seat per person |
| 2 | [Password manager](modules/password-manager.md) | Reused and shared passwords, recovery codes on sticky notes | A 1Password seat per person |
| 3 | Hardware keys ([#2](https://github.com/bulkhead-labs/opsec-baseline/issues/2)) | Sign-in that can be phished | Two keys per person |
| 4 | Super admin split ([#3](https://github.com/bulkhead-labs/opsec-baseline/issues/3)) | Daily accounts that can change everything | One more Workspace seat per admin; the keys from 3 |
| 5 | Least-privilege admin audit ([#4](https://github.com/bulkhead-labs/opsec-baseline/issues/4)) | Standing admin nobody needs | Time only |
| 6 | Phone and SIM hardening ([#5](https://github.com/bulkhead-labs/opsec-baseline/issues/5)) | SIM swaps and port-outs | Time only |
| 7 | AI connector scopes ([#7](https://github.com/bulkhead-labs/opsec-baseline/issues/7)) | Agents and connectors with more access than their job needs | Time only |

Modules 3 to 7 are planned. Each has an issue in the
[v0.1 milestone](https://github.com/bulkhead-labs/opsec-baseline/milestone/1).

## Use it with your agent

Give your agent a prompt that names a tag, the modules in order, your
tools, and where to keep the checklist. The agent reads
[`AGENTS.md`](AGENTS.md) and only the modules you name, and works through
them with you. For example, for an invented six-person team:

```
Work through Bulkhead Labs' OPSEC baseline with us.

Repo: https://github.com/bulkhead-labs/opsec-baseline at tag v0.1.
Read AGENTS.md at that tag first and follow its rules.
Modules, in this order: work-email, password-manager.
Our tools: Google Workspace Business Starter; the domain at Cloudflare;
Slack, GitHub, Notion, Figma, Stripe. No password manager yet.
Checklist: opsec-checklist.md in our private ops repo.
Extra guardrails: only Priya changes Google admin settings.
```

Agents that load skills can use [`skills/opsec-baseline`](skills/opsec-baseline/SKILL.md):
copy the folder into your agent's skills directory. It points back to
`AGENTS.md`, so every agent follows the same rules.

**Pin a tag.** A tag never changes, so the plan you started is the plan
you finish. [`CHANGELOG.md`](CHANGELOG.md) says what changed between
tags.

## Use it by hand

Read the modules in order. Each one has the same parts, described in
[`docs/module-format.md`](docs/module-format.md). Its "What done looks
like" list is your checklist.

## What this is not

- **Not a service.** It is guidance. Your team decides and your team
  acts. Nobody outside your team needs to log in to anything.
- **Not a security review.** It covers the basics most small teams skip.
  It doesn't look at your product, your code or your infrastructure.
- **No warranty.** Vendors change their consoles. Each module says when
  it was last checked. Modules name what you pay for, not the price:
  prices change too often, so check the vendor's page.

## Licence and credit

The text is under [CC BY 4.0](LICENSE): copy it, adapt it, use it with
clients, with credit. A credit line that works:

> Based on [OPSEC baseline](https://github.com/bulkhead-labs/opsec-baseline)
> by Bulkhead Labs, CC BY 4.0.

The licence covers the text, not the Bulkhead Labs name or logo. A copy
you change should not look as if it comes from Bulkhead Labs.

## From Bulkhead Labs

[Bulkhead Labs](https://bulkheadlabs.com) works with startups and small
businesses on security that keeps one breach from sinking the ship. After
a call, we build a team its own plan from these modules: the modules in
its order, why each one matters to it, and the prompt for its agent.
