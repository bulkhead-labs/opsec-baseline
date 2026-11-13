---
id: admin-split
title: Separate admin accounts
summary: Admin rights live on separate key-only accounts held by at least two people, plus one break-glass account; daily accounts hold none.
depends_on: [hardware-keys]
applies_to: [google-workspace, microsoft-365]
default: Google Workspace admin accounts, with the YubiKeys from hardware-keys
cost: One more Google Workspace seat per admin account, the break-glass account included, and two keys for the break-glass account
time: 2 hours for the admins; 15 minutes each quarter
checked: 2026-11-12
---

# Separate admin accounts

## The attack

The account a person uses every day is the one most likely to be
phished, so a super admin role on it hands every account and setting in
the company to whoever gets in, and with one admin, a lost key or a
departure can lock everyone out.

## Cost and time

| | Cost | Time |
|---|---|---|
| Admin accounts | One more Google Workspace seat per person who administers | 30 minutes each |
| Break-glass account | One more seat, and two keys of its own (ordered in `hardware-keys`) | 30 minutes |
| Moving the roles | | 30 minutes |
| Each quarter | | 15 minutes to test the break-glass account |

The admins reuse their own two keys from `hardware-keys`: one key holds
many accounts. For the current seat price, see Google's pricing page
(Sources).

This module covers the Google Workspace admin console. Admin rights in
other services (GitHub, Slack, the cloud account, billing) are for
`admin-audit`.

## What done looks like

- **D1.** Each person who administers Google Workspace has a separate
  admin account, for example `alex-admin@`, with both of their keys
  registered and under "Only security key". It is used only for admin
  work.
- **D2.** At least two people have an admin account with the Super
  Admin role.
- **D3.** A break-glass super admin account exists. It belongs to no one
  person, has two keys of its own, registered and stored in two
  different places, neither on a keychain. Its password is in the
  restricted 1Password vault (`password-manager` D6), and no backup codes
  are kept for it.
- **D4.** No daily account holds any admin role. `Admin console >
  Account > Admin roles` lists only admin accounts and the break-glass
  account as admins.
- **D5.** Super admin account recovery is off.
- **D6.** The break-glass account is tested each quarter: someone signs
  in with one of its keys, alternating keys each time, then signs out.
  The checklist has the date of the last test.
- **D7.** The offboarding list and the lost-key list cover admin
  accounts and the break-glass account.

## Steps

1. **Agent.** Ask an admin for the list in `Admin console > Account >
   Admin roles`: each role and who holds it. Compare it with the people
   who should administer. Propose who gets an admin account (at least
   two people), the names, the break-glass account's name (one that
   belongs to no person, for example `continuity@`), and where each of
   its keys will live. Give the seat cost. (D1, D2, D3)
2. **Person.** A super admin adds a user for each admin account and for
   the break-glass account in `Admin console > Directory > Users`, and
   puts each in the admins group or unit that has "Only security key"
   from `hardware-keys` D3. The new-user enrollment period lets each one
   sign in once to add keys. (D1, D3)
3. **Person, each one.** In a separate browser profile, sign in to your
   new admin account and register both of your keys, as in
   `hardware-keys` step 3. Sign out, then sign in with each key. Save
   the account's password in your private 1Password vault. (D1)
4. **Person.** A super admin gives each new admin account the Super
   Admin role: `Admin console > Directory > Users > (the admin account) >
   Admin roles and privileges`. Any other role a daily account holds
   moves to that person's admin account too. Each admin then signs in to
   `admin.google.com` with their admin account and a key, and says it
   works. (D1, D2)
5. **Person.** An owner of 1Password makes the break-glass password with
   1Password's generator and saves it in the restricted vault. Sign in to
   the break-glass account in a private window, register its two keys,
   and sign in once with each. A super admin gives it the Super Admin
   role. Don't print or save backup codes for it: its second key is its
   spare. (D3)
6. **Person.** Put the break-glass keys in two places that can't both be
   lost at once: for example one locked away at the office and one at a
   second admin's home, or in a bank deposit box. Neither goes on a
   keychain. Write down where each is, and who can reach it. (D3)
7. **Agent.** Check `Admin console > Account > Admin roles > Super
   Admin`: it should list at least two admin accounts and the break-glass
   account. Don't go on until it does. (D2, D3)
8. **Person.** Remove every admin role from each daily account, one
   person at a time, signed in with an admin account. Before each one,
   that person signs in to their own admin account and confirms it
   works. (D4)
9. **Person.** In `Admin console > Security > Authentication > Account
   recovery > Super admin account recovery`, turn it off. With three
   super admin accounts, each can recover the others. (D5)
10. **Person.** Each quarter, a super admin takes one break-glass key,
    signs in to the account in a private window, checks the sign-in shows
    in `Admin console > Reporting > Audit and investigation > User log
    events`, signs out, and puts the key back. Use the other key the next
    time. (D6)
11. **Agent.** Update the team's lists:
    - offboarding: when an admin leaves, suspend their admin account as
      well as their daily one; if they could reach a break-glass key,
      move the key; if they could see the restricted vault, change the
      break-glass password;
    - lost-key: an admin who loses both keys gets backup codes from
      another super admin; a lost break-glass key is removed from the
      account at once, and a new one is registered and stored;
    - the inventory: Google Workspace's admins are now the admin
      accounts. (D7)

## Agent instructions

- **Read first.** Step 1 is reading. Report what you find before
  proposing anything else.
- **Never remove the last working super admin.** Step 8 waits for step
  7. If a step leaves fewer than two working admin accounts plus the
  break-glass account, stop.
- **You get no admin account** and never hold or see the break-glass
  password or keys. Ask "is it in the restricted vault?" and record the
  answer.
- **Two people, not two accounts.** If only one person in the company
  can be trusted with admin, stop and ask who the second is: a
  co-founder, or another long-term person. One person with two accounts
  doesn't meet D2.
- **Admin accounts get Google's admin mail.** Suggest each admin add a
  secondary email contact to their admin account, as Google advises, so
  notices reach an inbox they read. Check the vendor's current help page
  for where.
- **Name the break-glass account plainly**, not after a person and not
  `admin@`. Its name will show in logs; nobody should be guessing whose
  it is.
- **If the break-glass account signs in outside a quarterly test**, it is
  an event. Ask who used it and why, and record the answer.
- **Never** ask for a password, a backup code or a key's PIN.

## Evidence

| Check | Record |
|---|---|
| D1 | Each admin account's name and its person, two keys on its Security page, its group or unit, the date |
| D2 | The admin accounts listed under the Super Admin role, and the date |
| D3 | The break-glass account's name, two keys on its Security page, where each key is kept and who can reach it, the password "in the restricted vault" with who confirmed |
| D4 | The `Account > Admin roles` list, each role's admins, all admin accounts, and the date |
| D5 | The super admin account recovery setting, and the date |
| D6 | The date of each test, which key, who did it, and that the sign-in showed in the log |
| D7 | Where the offboarding and lost-key lists are kept, and the date they were updated |

## Variants

### Microsoft 365

Microsoft's names and advice differ here:

- D1: Microsoft says admin-only accounts don't need a Microsoft 365
  licence, so they need no extra seat. It also advises a name that doesn't say
  the account is an admin, for example `alexc@` beside `alex.chen@`.
- D2: give the admin accounts the Global Administrator role, and other
  roles only where needed. Microsoft's "Add an administrator" page has
  the steps.
- D3: Microsoft asks for at least two emergency access accounts, not
  one. Each is cloud-only on the `.onmicrosoft.com` domain, holds Global
  Administrator, and signs in with a passkey on a security key of its
  own, not an admin's key. Store their keys in separate, secure places.
  Exclude them from any Conditional Access policy that blocks sign-in.
  Microsoft's business admin page still suggests leaving them out of
  multi-factor sign-in, with a long password; follow the Entra page
  instead, which names passkeys and says they meet Microsoft's required
  multi-factor sign-in.
- D5: this is Google's setting. Record it `not needed`: the admin
  accounts sign in with keys, and the emergency accounts are the
  recovery.
- D6: Microsoft asks for a test at least every 90 days, which the
  quarterly test meets.

## Why this default

- **This is Google's own advice:** more than one super admin, each a
  different person; a separate account for daily work; security keys on
  admin accounts.
- **A break-glass account**, because two admins can still both be away,
  both lose their keys, or both leave. Google's own recovery then works,
  but it asks for proof of the domain and takes time.
- **No backup codes for the break-glass account.** Codes next to its
  password would let someone with the vault in without a key. Its second
  key, kept elsewhere, is the spare.
- **Super admin recovery off.** Recovery by text message or email would
  be a weaker door than the key. Google's cloud guidance recommends
  keeping it off, and three super admin accounts can recover each other.
- **Given up:** a seat for each admin account and for the break-glass
  account, and a second sign-in whenever an admin needs the console.

## Sources

All checked 2026-11-12.

- [Google Workspace pricing](https://workspace.google.com/pricing): current seat prices.
- [Security best practices for administrator accounts](https://knowledge.workspace.google.com/admin/users/security-best-practices-for-administrator-accounts): more than one super admin, each a different person; a separate daily account; security keys; a spare key; the recovery wizard asks for proof of the domain; a secondary email contact.
- [Super administrator account best practices](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices): separate super admin accounts (`alice-admin@`); keep the key somewhere safe; keep self-recovery off.
- [Make a user an admin](https://knowledge.workspace.google.com/admin/users/make-a-user-an-admin) and [Assign specific admin roles](https://knowledge.workspace.google.com/admin/users/assign-specific-admin-roles): `Directory > Users > Admin roles and privileges`; `Account > Admin roles`.
- [Allow super administrators to recover their password](https://knowledge.workspace.google.com/admin/users/allow-super-administrators-to-recover-their-password): `Security > Authentication > Account recovery > Super admin account recovery`.
- [Manage a user's security settings](https://knowledge.workspace.google.com/admin/security/manage-a-users-security-settings): only super admins make backup codes for other admins.
- [User log events](https://knowledge.workspace.google.com/admin/reports/user-log-events): `Reporting > Audit and investigation > User log events`.
- [Manage emergency access admin accounts](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access): two or more, cloud-only, passkeys (FIDO2), separate secure storage, Conditional Access exclusions, test at least every 90 days.
- [Admin account security in Microsoft 365 for business](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-account-security-admins): admin-only accounts need no licence; a name that doesn't advertise admin; its advice on emergency accounts, which the Entra page supersedes.
