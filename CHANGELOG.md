# Changelog

What changed in each tag. A team's plan names a tag, so a change here
never changes a plan a team already has.

## Next tag (v0.2, unreleased)

- `hardware-keys`: the time now says that the admin's 2 hours is
  one-time company setup over two weeks, and that the 30 minutes per
  person includes the admin. Step 3 sets up each key first: check it
  has no PIN, set a PIN of 8 characters or more, then keep the daily key
  on you and store the spare. "Always require user verification" stays
  off. New check D9: every key has a PIN.
- `admin-split`: separate admin accounts now cover every highly
  sensitive service, not just Google Workspace. A service is highly
  sensitive if its admin can change who signs in, move money, or reach
  production and its customer data. New checks D8 to D11: the list of
  those services, admin roles on `-admin@` accounts where the service
  signs in with Google, a separate admin login where it has its own,
  and a written reason where neither works (the password manager and
  GitHub are named). New steps 12 to 16.
- `admin-audit`: D3 and "Why this default" now point to `admin-split`
  for highly sensitive services.
- `AGENTS.md`: a check the team's plan leaves out is recorded as
  `not needed`, with the reason "out of scope in our plan".
- Seven Walls: the time and cost lines for walls 3 and 4.

## v0.1 (2026-11-13)

- The module format, `AGENTS.md` and the `opsec-baseline` skill.
- `work-email`: work email, and sign in with Google.
- `password-manager`: password manager, which also holds recovery codes.
- `hardware-keys`: two keys per person, and Google sign-in by key only.
- `admin-split`: separate admin accounts, and a break-glass account.
- `admin-audit`: who is admin where, cut to what the work needs.
- `phone-sim`: carrier locks and PINs, and no text-message sign-in.
- `ai-connector-scopes`: each AI tool and connector at the least it needs.
- Seven Walls, the story page on GitHub Pages.
