---
id: admin-split
title: Separate admin accounts
summary: Admin rights live on separate key-only accounts held by at least two people, plus one break-glass account, in Google Workspace and every other highly sensitive service; daily accounts hold none.
depends_on: [hardware-keys]
applies_to: [google-workspace, microsoft-365]
default: Google Workspace admin accounts, with the YubiKeys from hardware-keys
cost: One more Google Workspace seat per admin account, the break-glass account included; two keys for the break-glass account; and an extra account in any other highly sensitive service that charges per account
time: 2 hours for the admins, plus 20 minutes per admin in each other highly sensitive service; 15 minutes each quarter
checked: 2026-11-14
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
| Other highly sensitive services | One more Workspace seat for each person who administers one of them but has no admin account yet, and an extra account in any service that charges per account | 20 minutes per admin, per service |
| Each quarter | | 15 minutes to test the break-glass account |

The admins reuse their own two keys from `hardware-keys`: one key holds
many accounts. For the current seat price, see Google's pricing page
(Sources). For another service, its own pricing page says whether it
charges per account: 1Password Business does, a seat per account; AWS
IAM and IAM Identity Center don't.

D1 to D7 cover the Google Workspace admin console. D8 to D11 carry the
same split to the other highly sensitive services. Who holds which role
in each of them, and in every other service, is for `admin-audit`.

## What done looks like

- **D1.** Each person who administers Google Workspace has a separate
  admin account, for example `theo-admin@` beside `theo@`, with both of
  their keys registered and under "Only security key". It is used only
  for admin work.
- **D2.** At least two people have an admin account with the Super
  Admin role, and each of them is a 1Password owner. Owners stay off
  Unlock with SSO (`password-manager` D4), so they can still open the
  restricted vault, and the break-glass password, if Google sign-in is
  the thing that broke.
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

**Highly sensitive services.** A service is highly sensitive if a
person with its admin or owner role can do any one of these:

- change who can sign in to the company's accounts: the password
  manager, the domain registrar and the DNS host (they control the
  company's mail, and with it every password reset);
- move the company's money: the bank, the payment tool, payroll;
- change production, or reach the customer data in it: the cloud
  account, and the code host that deploys to it.

Google Workspace is the first of them; D1 to D7 cover it. Ask the same
three questions of every other service on the `work-email` inventory.
A yes to any one makes it highly sensitive. A tool that holds only a
copy of some customer data, like the chat workspace, a CRM or a help
desk, is not on the list: `admin-audit` keeps its admins few and on
keys.

- **D8.** The checklist lists every highly sensitive service, each with
  the question it answers yes to and its setup: through Google (D9), a
  separate login (D10), or a written reason for neither (D11).
- **D9.** In each highly sensitive service that signs in with Google,
  every admin or owner role is held only by `-admin@` accounts. Each
  person's daily account there is a plain member, or has no account.
- **D10.** In each highly sensitive service with its own login, each
  admin does admin work from a separate login on their `-admin@`
  address, with both of their keys where the service takes them. Their
  daily login there, if they have one, holds no admin role.
- **D11.** Each highly sensitive service with neither setup has the
  reason written in the checklist: one of the two named under Agent
  instructions, or the service allows only one login per person. Each
  admin's one login there has two-step verification, with their keys
  where the service takes them (`admin-audit` D5).

## Steps

1. **Agent.** Ask an admin for the list in `Admin console > Account >
   Admin roles`: each role and who holds it. Compare it with the people
   who should administer. Propose who gets an admin account (at least
   two people, each a 1Password owner), the names, the break-glass
   account's name (one that belongs to no person, for example
   `continuity@`), and where each of its keys will live. Give the seat
   cost. (D1, D2, D3)
2. **Person.** A super admin adds a user for each admin account and for
   the break-glass account in `Admin console > Directory > Users`, and
   puts each in the admins group or unit that has "Only security key"
   from `hardware-keys` D3. Its new user enrollment period lets each one
   sign in once to add keys. If a new account can't (the period has
   passed), a super admin makes backup codes for it in `Directory >
   Users > (the account) > Security > 2-Step Verification > Get backup
   verification codes`; for the break-glass account, keep none once its
   keys are on. Moving an existing user into the group gives it no
   enrollment window. (D1, D3)
3. **Person, each one.** In a separate browser profile, sign in to your
   new admin account and register both of your keys, as in
   `hardware-keys` step 3. Sign out, then sign in with each key. Save
   the account's password in your private 1Password vault. (D1)
4. **Person.** A super admin gives the Super Admin role only to the
   admin accounts of the people named for D2: `Admin console >
   Directory > Users > (the admin account) > Admin roles and
   privileges`. If one of them isn't a 1Password owner yet, an owner
   makes them one first, unlocking with a password, not Google
   (`password-manager` D4). The new owner then does `password-manager`
   step 7: an account password, two-factor, and the Emergency Kit. Any other admin account gets the narrower
   role its person needs, as in `admin-audit` D2. A role a daily
   account holds moves to that person's admin account too. Each admin
   then signs in to `admin.google.com` with their admin account and a
   key, and says it works. (D1, D2)
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
   account. In 1Password, check that each person behind those admin
   accounts is in the Owners group. Don't go on until both hold.
   (D2, D3)
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
      another super admin; if the break-glass account must be used
      without its keys, another super admin makes backup codes for it;
      a lost break-glass key is removed from the account at once, and a
      new one is registered and stored;
    - the inventory: Google Workspace's admins are now the admin
      accounts. (D7)
12. **Agent.** Ask the three questions under "Highly sensitive
    services" of each service on the `work-email` inventory, and list
    the ones that answer yes. For each, look up on the vendor's own help
    pages whether it signs in with Google, and whether it allows a
    second login for the same person. Propose one setup for each: D9 if
    it signs in with Google, D10 if it has its own login and allows a
    second one, D11 with the reason otherwise, including the two named
    under Agent instructions. List who needs an
    `-admin@` account they don't have yet, and give the cost: a
    Workspace seat for each, and an extra account where the service
    charges per account. (D8)
13. **Person.** For each person who administers one of these services
    but not Google Workspace, a super admin adds their `-admin@` account
    as in step 2, with no Google admin role, and the person does step 3.
    (D9, D10)
14. **Person, each one.** Service by service, while your daily account
    still holds its role:
    - **Signs in with Google (D9).** If Google controls who can use the
      service, a Google admin turns it on for your admin account (for a
      SAML app: `Admin console > Apps > Web and mobile apps > (the app)
      > User access`). An admin of the service adds your
      `-admin@` account with the role your daily account has. Sign in
      with it and a key, and say it works.
    - **Own login (D10).** Make a new login on your `-admin@` address,
      with a password from 1Password's generator saved in your private
      vault. Turn on two-step verification and add both of your keys, or
      an authenticator app where it takes no keys; recovery codes go in
      your private vault. An admin of the service gives the new login
      the role. Sign in once with each key, and say it works.

    Then an admin who stays lowers your daily account to a plain member,
    or removes it. Keep at least two people with the top role at every
    point (`admin-audit`). (D9, D10)
15. **Person, each one.** At each D11 service, check that your one login
    has two-step verification on, with both of your keys where it takes
    them, and say so. (D11)
16. **Agent.** Add each admin login from steps 13 and 14 to the
    offboarding and lost-key lists from step 11, and record each
    service's setup in the checklist. (D7, D8)

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
- **One setup per highly sensitive service**, in this order: through
  Google if the service signs in with Google (D9); a separate login if
  it has its own and allows a second one (D10); otherwise a written
  reason (D11). If a service could sign in with Google but doesn't yet,
  don't start that change here: use its own login and note the option.
- **Two reasons for D11 are already decided:**
  - **The password manager.** 1Password owners already sign in with
    their own account password, Secret Key and keys, not through Google
    (`password-manager` D4, `hardware-keys` D5), so a caught daily
    Google account doesn't reach the owner role. A second 1Password
    account would be another seat and another vault to keep. Record:
    "owners sign in without Google".
  - **GitHub.** Its terms allow one free personal account per person,
    and GitHub advises one personal account for all work. Owners keep
    the role on their own account, with both keys, and the organization
    requires two-factor for everyone (`Settings > Authentication
    security > Require two-factor authentication for everyone in your
    organization`). Record: "one account per person by GitHub's terms".
    A team on GitHub Enterprise with its own sign-in is different; ask.
- **A bank or payroll login** is often one per person. If its help
  pages or its support say so, that is the D11 reason. Never start an
  account change at a bank yourself.
- **Never lower a daily account first.** The admin login works before
  the daily one loses its role, every time.
- **Never** ask for a password, a backup code or a key's PIN.

## Evidence

| Check | Record |
|---|---|
| D1 | Each admin account's name and its person, two keys on its Security page, its group or unit, the date |
| D2 | The admin accounts listed under the Super Admin role, that each of their people is in 1Password's Owners group, and the date |
| D3 | The break-glass account's name, two keys on its Security page, where each key is kept and who can reach it, the password "in the restricted vault" with who confirmed |
| D4 | The `Account > Admin roles` list, each role's admins, all admin accounts, and the date |
| D5 | The super admin account recovery setting, and the date |
| D6 | The date of each test, which key, who did it, and that the sign-in showed in the log |
| D7 | Where the offboarding and lost-key lists are kept, and the date they were updated |
| D8 | Each highly sensitive service, the question it answers yes to, its setup (D9, D10 or D11), and the date |
| D9 | For each such service: its admin role list showing only `-admin@` accounts, each daily account a plain member or absent, and the date |
| D10 | For each such service and admin: the admin login's address, two-step on with keys or an app, the daily login's role, from their yes and the role list, and the date |
| D11 | For each such service: the reason, and for each admin, two-step on there, with keys or an app, from their yes and the date |

## Variants

### Microsoft 365

Microsoft's names and advice differ here:

- D1: Microsoft says admin-only accounts don't need a Microsoft 365
  licence, so they need no extra seat. It also advises a name that doesn't say
  the account is an admin, for example `theo.r@` beside `theo@`.
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
- D8 to D11: the same, with "signs in with Microsoft" in place of
  Google, and the admin account from D1 as the admin identity.

## Why this default

- **This is Google's own advice:** more than one super admin, each a
  different person; a separate account for daily work; security keys on
  admin accounts.
- **A break-glass account**, because two admins can still both be away,
  both lose their keys, or both leave. Google's own recovery then works,
  but it asks for proof of the domain and takes time.
- **No backup codes for the break-glass account.** Codes next to its
  password would let someone with the vault in without a key. Its second
  key, kept elsewhere, is the spare. If both keys are gone, another
  super admin can make backup codes for it: that is the way back.
- **Super admin recovery off.** Recovery by text message or email would
  be a weaker door than the key. Google's cloud guidance recommends
  keeping it off, and three super admin accounts can recover each other.
- **Every highly sensitive service, not just Google.** A caught admin
  session at the bank, the cloud account or the registrar reaches as
  far as a Google super admin: the money, every customer, or everyone's
  sign-in. The three questions keep the list short, so the split costs
  a few accounts, not one per tool.
- **Through Google first.** Where a service signs in with Google, the
  `-admin@` account brings its keys and its "Only security key" policy
  with it, and suspending it in Google closes it everywhere.
- **Given up:** a seat for each admin account and for the break-glass
  account, an extra account in some services, and a second sign-in
  whenever an admin needs a console. GitHub and the password manager
  keep the role on one account, with keys.

## Sources

All checked 2026-11-12, except where a line says 2026-11-14.

- [Google Workspace pricing](https://workspace.google.com/pricing): current seat prices.
- [Security best practices for administrator accounts](https://knowledge.workspace.google.com/admin/users/security-best-practices-for-administrator-accounts): more than one super admin, each a different person; a separate daily account; security keys; a spare key; the recovery wizard asks for proof of the domain; a secondary email contact. Checked 2026-11-14: "a separate, non-admin account for day-to-day activities".
- [Super administrator account best practices](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices): separate super admin accounts (`alice-admin@`); keep the key somewhere safe; keep self-recovery off.
- [Make a user an admin](https://knowledge.workspace.google.com/admin/users/make-a-user-an-admin) and [Assign specific admin roles](https://knowledge.workspace.google.com/admin/users/assign-specific-admin-roles): `Directory > Users > Admin roles and privileges`; `Account > Admin roles`.
- [Allow super administrators to recover their password](https://knowledge.workspace.google.com/admin/users/allow-super-administrators-to-recover-their-password): `Security > Authentication > Account recovery > Super admin account recovery`.
- [Manage a user's security settings](https://knowledge.workspace.google.com/admin/security/manage-a-users-security-settings): only super admins make backup codes for other admins.
- [User log events](https://knowledge.workspace.google.com/admin/reports/user-log-events): `Reporting > Audit and investigation > User log events`.
- [Manage emergency access admin accounts](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access): two or more, cloud-only, passkeys (FIDO2), separate secure storage, Conditional Access exclusions, test at least every 90 days.
- [Admin account security in Microsoft 365 for business](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-account-security-admins): admin-only accounts need no licence; a name that doesn't advertise admin; its advice on emergency accounts, which the Entra page supersedes.
- [Set up your own custom SAML app](https://knowledge.workspace.google.com/admin/apps/set-up-your-own-custom-saml-app): `Apps > Web and mobile apps > (the app) > User access`, on or off per organizational unit or access group. Checked 2026-11-14.
- [1Password Business pricing](https://1password.com/business-pricing): a seat per user. Checked 2026-11-14.
- [IAM Identity Center FAQs](https://aws.amazon.com/iam/identity-center/faqs/) and [IAM FAQs](https://aws.amazon.com/iam/faqs/): both at no extra charge. Checked 2026-11-14.
- [Use Google Workspace with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/gs-gwp.html): AWS sign-in through Google Workspace; turn the app on only for the users who need it. Checked 2026-11-14.
- [AWS MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html): IAM users take up to eight MFA devices, security keys included. Checked 2026-11-14.
- [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service): "no more than one free Account" per person. Checked 2026-11-14.
- [GitHub account management](https://docs.github.com/en/account-and-profile/concepts/account-management): "use one personal account for all your work on GitHub.com". Checked 2026-11-14.
- [Requiring two-factor authentication in your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization): `Settings > Authentication security`. Checked 2026-11-14.
