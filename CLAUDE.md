# CLAUDE.md

opsec-baseline: public OPSEC modules from Bulkhead Labs. Each module is
one fix a small team makes itself, with steps its own agent can follow.
This file is for agents **maintaining the repo**. An agent helping a team
work through the modules reads [`AGENTS.md`](AGENTS.md) instead.

Read [`README.md`](README.md), [`docs/module-format.md`](docs/module-format.md)
and the modules you are touching before doing anything.

## Rules

1. **This repo is public.** Never commit, or put in an issue, PR or
   comment: secrets; the name of any client, prospect or person Bulkhead
   Labs has spoken with; anything said on a call; anything from a team's
   plan or checklist. Examples use invented teams.
2. **Bulkhead Labs branding only.** Never a client's name, logo or
   branding. The logo files in `assets/` come from Bulkhead's brand kit;
   don't edit them here.
3. **Guidance only.** Modules tell a team how to do the work. They never
   say that Bulkhead Labs, or anyone outside the team, will log in, buy
   anything or administer users or devices.
4. **One answer per module.** Name one default vendor. Add a fallback only
   for a specific need, and name the need.
5. **No prices.** They go stale. Say what the team pays for (a seat per
   person, two keys per person) and link the vendor's pricing page.
   Vendor facts and console paths carry a source: the vendor's own help
   pages only. Update `checked:` whenever you re-check them.
6. **Ids are stable.** A module's `id` and its check numbers (`D1`, ...)
   never change once a tag contains them. Teams' plans name them.
7. **Tags are fixed.** Never move or delete a tag. A change after a tag
   ships in the next tag, and the changelog says what changed.
8. **Agent-agnostic.** Plain markdown, `AGENTS.md` as the entry point,
   skills in `skills/` in the open `SKILL.md` format. Nothing that only
   one vendor's agent can read.
9. **Every step can be checked.** If a person can't verify a check by
   looking at a setting or a list, rewrite it.
10. **Sign off every commit** (`git commit -s`). PRs open as drafts, are
    reviewed by the maintainer, and are squash-merged only when the
    maintainer asks.

## Working here

- **Work is tracked in this repo's issues**, one per module or change,
  grouped by milestone (`v0.1`, ...). A PR says `Closes #n`.
- **A new module:** copy `docs/module-template.md` to `modules/<id>.md`,
  fill every section, add it to the index in `modules/README.md` and the
  table in `README.md`, and add a line to `CHANGELOG.md`.
- **Check the console paths** against the vendor's current help pages
  when you write or change a step. Link the page in Sources.
- **Before a PR is ready:** read every changed module as the founder
  (could I decide from this?) and as the agent (could I follow this
  without guessing, and without touching a secret?). Then search the
  diff for names, addresses and anything that looks like a client.
- **The story page** is the plain-language version of the modules,
  served by GitHub Pages from `docs/`. Its source is `site/src/`: the
  scenes, styles and script that `gen.py` turns into `site/story.html`.
  Edit `site/src/`, run `python3 site/build.py`, and commit the
  regenerated `site/story.html` and `docs/index.html` with it.
  A module change that alters a chapter's story, time or cost updates
  the chapter in the same PR. Analogies only where they really fit.
- **Style:** short sentences, plain words, no scare words. Console paths
  in the form `Admin console > Security > ...`.
