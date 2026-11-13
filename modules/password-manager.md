---
id: password-manager
title: Password manager
summary: One company password manager for every login Google sign-in doesn't cover, every shared login, and every recovery code.
depends_on: [work-email]
applies_to: [any]
default: 1Password Business
fallback: Bitwarden Enterprise, only if the team must host it itself
cost: A 1Password Business subscription per person
time: 2 hours for the admin; 30-60 minutes per person
checked: 2026-11-12
---

# Password manager

## The attack

When one password is used in several places, a leak from any one of
them opens all the others, and a recovery code in a notes app or a photo
is a spare key to the most important account the company has.

## Cost and time

| | Cost | Time |
|---|---|---|
| 1Password Business | A subscription per person | 2 hours for the admin to set up |
| Per person | Included: a free 1Password Families account for home | 30-60 minutes to move their passwords in |

No hardware needed. For the current price, see 1Password's pricing page
(Sources).

## What done looks like

- **D1.** The company has a 1Password Business account, created with a
  company address, with at least two people in the Owners group.
- **D2.** Every person who works for the company is a member, invited at
  their company address. Nobody who has left is.
- **D3.** At least two people can recover a member's account: owners,
  administrators, or a group given the "Recover Accounts" permission.
- **D4.** Everyone except the owners unlocks 1Password with their Google
  account (Unlock with SSO). The owners keep their account password and
  Secret Key, as 1Password requires, and two-factor is enforced for them
  **(later: `hardware-keys` adds a key to each owner's account)**.
- **D5.** Each owner has saved their Emergency Kit offline: printed and
  put away, not a photo, not a cloud document.
- **D6.** Vaults are set up by purpose: one shared vault per group of
  shared logins, and a restricted vault, Owners only, for recovery codes
  and the domain registrar.
- **D7.** Every service the `work-email` inventory marks `password` has
  its login in 1Password, with a unique generated password. Shared logins
  live in a shared vault, not in a chat, a document or a browser. This
  finishes `work-email` D3.
- **D8.** The company's recovery codes (Google Workspace admins, the
  domain registrar, the DNS host, the admin or billing login of each
  core service) are in the restricted vault. Each person's own recovery
  codes are in their private vault. Every other copy is deleted. This
  finishes `work-email` D1.
- **D9.** Each person has moved the passwords saved in their browser
  into 1Password and turned off the browser's offer to save passwords.

## Steps

1. **Person.** An owner starts a 1Password Business account, using a
   company address. (D1)
2. **Person.** Set the password policy to Strict. 1Password requires it
   before two-factor can be enforced. (D4)
3. **Person.** An owner sets up Unlock with SSO with Google Workspace,
   following 1Password's Google guide, for everyone. Owners are left out
   automatically. Do this before inviting anyone, so people join with
   their Google sign-in. (D4)
4. **Agent.** From the `work-email` user list, draft the list of people
   to invite and the vaults to create. Suggest vaults by purpose, for
   example `Shared - Operations`, `Shared - Marketing`, and `Restricted -
   Recovery` for the owners. Show it for a yes. (D2, D6)
5. **Person.** Create the vaults, set who can see each one, and invite
   every person, owners included. (D2, D6)
6. **Person, each one.** Accept the invitation and sign in with Google.
   Install the browser extension and the phone app; each new one asks
   for a code from one you've already linked. (D4)
7. **Person, each owner.** Set a long account password you don't use
   anywhere else, turn on two-factor, and save the Emergency Kit: print
   it and put it away. (D4, D5)
8. **Person.** Once the second owner has accepted, add them to the
   Owners group. Check that at least two people can recover accounts:
   the two owners count. Then enforce two-factor authentication. It
   applies to everyone who signs in with a password: the owners. (D1,
   D3, D4)
9. **Person, each one.** Import the passwords saved in your browser,
   then delete them from the browser and turn off its offer to save
   passwords. (D9)
10. **Agent.** From the inventory, list every service marked `password`
   and every login the team says is shared, with the vault each one
   belongs in. Don't ask for the passwords. (D7)
11. **Person, each one.** For each service on that list: sign in, change
    the password to one 1Password generates, and save it in the vault the
    list says. Where Google sign-in left an old password behind, replace
    it with a generated one too. A service that `work-email` left on a
    shared account can now move to the shared vault, and the shared
    account can be closed (`work-email` D3). (D7)
12. **Agent.** List the recovery codes to move, and ask where each set is
    kept now (a notes app, a photo, a document, paper):
    - the company's: each Google Workspace admin, the domain registrar,
      the DNS host, and the admin or billing login of each core service;
    - each person's own: their Google backup codes from `work-email`, and
      any service they turned two-step verification on for. (D8)
13. **Person.** An owner puts the company's recovery codes in the
    restricted vault. (D8)
14. **Person, each one.** Put your own recovery codes in your private
    vault. Then delete every other copy of every set, including photos
    and their cloud backups. Where you can't find the codes, make a new
    set in the service, which cancels the old ones. (D8)
15. **Agent.** Update the inventory: each `password` service now says
    which vault holds it. Update the offboarding list: remove the person
    from 1Password, and change every shared password they could see.
    (D2, D7)

## Agent instructions

- **You never see a vault.** Don't ask for access to 1Password, its
  command-line tool or a service account for this module. Work from the
  inventory and from what people tell you.
- **Never ask for a password or a code**, not even to check it works.
  Ask "is it saved in the vault?" and record the answer.
- **Owners and recovery come first** (steps 1 to 8), before anyone moves
  a password in. A vault with one owner and no recovery is one forgotten
  password from gone.
- **Two-step codes for shared logins** (a shared social account, a
  shared supplier portal) can go in the shared vault beside the login,
  so the team can use them. For a person's own accounts, and every admin
  account, prefer a passkey or, once `hardware-keys` is done, a key.
  Say this when you propose step 11.
- **Unlock with SSO goes on before anyone is invited** (step 3). Only
  set it up once `work-email` D4 (2-Step Verification enforced) is done:
  the Google sign-in now guards the vaults too.
- **Stop and ask** if nobody can find the recovery codes for a Google
  admin or the registrar. Making new ones is a person's step, done while
  signed in.

## Evidence

| Check | Record |
|---|---|
| D1 | The account's sign-in address domain, and the names of the owners |
| D2 | The member count, and that it matches the `work-email` user list |
| D3 | The names of the people who can recover accounts, and their role or group |
| D4 | Unlock with SSO: on, for everyone; the two-factor policy setting and the date it took effect |
| D5 | Each owner's yes, with the date. Not the kit |
| D6 | The vault names and who can see each one |
| D7 | For each `password` service: the vault it's in, and the date the password was changed |
| D8 | For each set on the step 12 list: "in the restricted vault" or "in the person's own private vault", "other copies deleted", who confirmed, the date |
| D9 | Each person's yes, with the date |

## Variants

### Bitwarden

Use Bitwarden only if the team must host its password manager on its
own servers. The checks are the same. Bitwarden's names: organizations
for the account, collections for vaults, and account recovery
administration for D3. Announce the two-step login policy a week before
turning it on: it cuts off members who haven't set it up.

It needs Bitwarden Enterprise, even in Bitwarden's cloud: account
recovery (D3), the policies behind D4, and self-hosting are on
Enterprise only. Bitwarden Teams has none of them (checked 2026-11-12).

## Why this default

- **1Password Business**, because the parts that matter for a small team
  work without setup: the Secret Key alongside the account password,
  account recovery by owners, a free family account that keeps work and home
  apart, and apps that people actually use.
- **One password manager, company-owned.** Personal password managers
  can't be audited or offboarded.
- **Unlock with SSO for everyone but the owners.** One sign-in to
  protect instead of two, and removing someone from Google removes them
  from 1Password too. A stolen Google sign-in alone doesn't open a vault:
  each new device needs a code from one the person already linked. Once
  `hardware-keys` is done, the vaults are behind a key. The owners stay
  on password and Secret Key, so the company still has a way in if the
  Google account is ever the problem.
- **Given up:** two-step codes for shared logins sit in the same vault as
  their passwords. Someone who gets into the vault gets both. For shared
  logins, that is the price of the team using them at all.

## Sources

All checked 2026-11-12.

- [1Password business pricing](https://1password.com/business-pricing): current prices; Business includes a free Families account per member.
- [Recover accounts for team members](https://support.1password.com/recovery/): owners, administrators and groups with the "Recover Accounts" permission; have at least two.
- [Emergency Kit](https://support.1password.com/emergency-kit/): what it holds.
- [Manage two-factor authentication](https://support.1password.com/manage-two-factor-authentication/): enforcing two-factor for everyone needs the Strict password policy.
- [Two-factor authentication](https://support.1password.com/two-factor-authentication/): authenticator app, security key or Duo.
- [Passkeys](https://support.1password.com/save-use-passkeys/) and [one-time passwords](https://support.1password.com/one-time-passwords/).
- [Unlock with SSO and Google](https://support.1password.com/sso-configure-google/): who it applies to; owners always keep password and Secret Key.
- [Switch to Unlock with SSO](https://support.1password.com/sso-get-started/) and [linked apps and browsers](https://support.1password.com/sso-linked-apps-browsers/): no Secret Key for SSO members; a new device needs a code from a linked one.
- [Bitwarden business pricing](https://bitwarden.com/pricing/business/): current prices; account recovery, policies and self-hosting on Enterprise only.
