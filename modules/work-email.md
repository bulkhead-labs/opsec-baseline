---
id: work-email
title: Work email, and sign in with Google
summary: Everyone works from a company account, and signs in to every service that allows it with that account.
depends_on: []
applies_to: [google-workspace, microsoft-365]
default: Google Workspace Business Starter
cost: $7 per person per month (Google Workspace Business Starter, annual plan)
time: Half a day for the admin; 30 minutes per person
checked: 2026-11-12
---

# Work email, and sign in with Google

## The attack

When people work from personal accounts and sign up for each tool with
its own password, one phished or reused password opens that tool, and
when someone leaves there is no single place to take their access back.

## Cost and time

| | Cost | Time |
|---|---|---|
| Google Workspace Business Starter | $7 per person per month on the annual plan, $8.40 on the flexible (monthly) plan; up to 300 people | |
| Shared addresses (`hello@`, `billing@`) | Free, as Google Groups | 10 minutes each |
| Email authentication (SPF, DKIM, DMARC) | Free | 1 hour, then a two-week wait |
| The service inventory and moving sign-ins | Free | 2-3 hours for the admin, with the agent |
| Per person | | 30 minutes to move their tools to Google sign-in |

Already on Google Workspace: this module costs time only. Not yet on it:
add the seats, and an afternoon to move mail (Google's own migration
tool does it). Prices checked 2026-11-12; sources below.

Some services charge more for single sign-on (SAML). This module doesn't
ask for it. The free "Sign in with Google" button is enough.

## What done looks like

- **D1.** The domain's registrar account, and the DNS host's if it is
  a separate one, belong to a company address (a group, so more than one
  person gets its mail), not a person's own. Each has two-step
  verification on, and the registrar has the transfer lock on. Their
  recovery codes go in the password manager **(later:
  `password-manager` D8)**.
- **D2.** Every person who works for the company has a Google Workspace
  account on the company domain. No company work lives in a personal
  account.
- **D3.** Shared addresses (`hello@`, `billing@`, `security@`) are
  Google Groups, not shared accounts with a password. A shared account
  that a single-login service still needs may stay until
  `password-manager` holds that login **(later: `password-manager`
  D7)**.
- **D4.** 2-Step Verification is enforced for every user, with any
  method except text messages and phone calls **(later: `hardware-keys`
  moves it to keys)**.
- **D5.** A service inventory exists: every service the company uses,
  who owns it, how people sign in (Google, password, other), and who is
  admin.
- **D6.** Every service on the inventory that offers "Sign in with
  Google" uses it, for every person. The rest are marked `password` and
  move to the password manager **(later: `password-manager` D7)**.
- **D7.** SPF, DKIM and DMARC are published for the domain, and the
  DMARC policy is `quarantine` or `reject`.
- **D8.** A written offboarding list says how to remove a person: suspend
  the Google account, then the services on the inventory that keep
  their own sessions or passwords.

## Steps

1. **Agent.** Ask who controls the domain, where it is registered, and
   where its DNS is hosted. Ask for a description, or a screenshot with
   no codes in it, of each account's owner address, two-step setting
   and, at the registrar, the transfer lock. (D1)
2. **Person.** Where an account is under a personal address, change it
   to a company group address. Turn on two-step verification with an
   authenticator app, and turn on the transfer lock. Leave the recovery
   codes where they are for now. The next module moves them. (D1)
3. **Agent.** List the users in `Admin console > Directory > Users`, or
   ask the admin for the list. Compare it with the people who work for
   the company. Note anyone missing, anyone who has left, and any
   shared account. (D2, D3)
4. **Person.** Create accounts for anyone missing. Suspend anyone who has
   left. Leave shared accounts alone until step 9. (D2)
5. **Agent.** Build the service inventory, with the team:
   - the apps people have signed in to with Google: `Admin console >
     Reporting > Audit and investigation > OAuth log events`, with the
     date range widened from its default of the last week, and `Admin
     console > Security > Access and data control > API controls >
     Manage App Access > Accessed apps`;
   - each person's own list at `myaccount.google.com/connections`;
   - the card and invoice statements of the last twelve months;
   - asking each person what they use for work, including what each
     shared account signs in to.

   For each service record the owner, how people sign in (`google`,
   `password` or `other`), who is admin, and whether it offers "Sign in
   with Google". Keep it in the team's private workspace, next to the
   checklist. (D5)
6. **Person.** Turn on 2-Step Verification in `Admin console > Security >
   Authentication > 2-step verification`:
   - allow users to turn it on;
   - set the methods to "Any except verification codes via text, phone
     call";
   - set enforcement to start on a date one week out;
   - set a new-user enrollment period of one week, so people added later
     have time to enrol.

   Tell everyone the date, and that anyone using text-message codes must
   switch before it or be locked out. Check that every admin can sign in
   with the new methods before the date. (D4)
7. **Person, each one.** Before the date, turn on 2-Step Verification
   for your own account with Google's prompt on your phone or an
   authenticator app, add a second method, and save your backup codes.
   Keep the codes on paper for now; the next module moves them. (D4)
8. **Person, each one.** For each service the inventory marks as
   offering it, switch your sign-in to "Sign in with Google". Where the
   service lets you, remove the old password; where it doesn't, the next
   module replaces it with a random one in the password manager. (D6)
9. **Person.** For each shared account: first move every service it
   signs in to onto a named person's account. A service that allows only
   one login stays on the shared account until `password-manager` holds
   it. Then rename the shared user (for example to `hello-old@`), create
   a Google Group on the old address (`Admin console > Directory >
   Groups`) with the right members, and delete the old user once its
   mail is moved. (D3)
10. **Agent.** Draft the SPF, DKIM and DMARC records, starting from the
   services on the inventory that send mail as the domain (Google, and
   often a newsletter tool, a CRM, a billing tool):
   - SPF: one TXT record that includes Google and each of those senders.
   - DKIM: generated in `Admin console > Apps > Google Workspace > Gmail >
     Authenticate email`, with a 2048-bit key; each other sender has its
     own DKIM setup in its settings.
   - DMARC: `v=DMARC1; p=none; rua=mailto:<a group address>` to start.
     The reports come from outside the company, so the group must let
     anyone outside post to it, or they bounce.

   Show the drafts and where each one goes. (D7)
11. **Person.** Add the records at the DNS host. Wait until the DKIM
    record shows up (it can take up to 48 hours), then press "Start
    authentication" in the Admin console. (D7)
12. **Agent.** Two weeks later, read the DMARC reports sent to the group
    address, if the team shares them with you. List any sender that
    fails SPF or DKIM. Once everything that should send passes, propose
    `p=quarantine`. (D7)
13. **Person.** Change the DMARC policy to `quarantine`. (D7)
14. **Agent.** Draft the offboarding list from the inventory: suspend the
    Google account; then, for each service that keeps its own password
    or keeps sessions open after Google sign-in stops, remove the person
    there; then move ownership of their files and groups. (D8)

## Agent instructions

- **Read first.** Steps 1, 3 and 5 are reading. Do them before
  proposing anything else, and report what you found. Draft steps 10, 12
  and 14 when you reach them.
- **The admin console is a person's.** Even with admin access, don't
  change users, groups, 2-Step Verification, DNS or DKIM. Draft the
  change, and let a person make it.
- **Don't lock out the admins.** Before enforcement starts (step 6),
  check that every admin has 2-Step Verification working. If there is
  one admin, say so: the `admin-split` module adds a second, but until
  then, a lost phone can lock the company out. When someone other than
  an admin loses their phone, an admin can make backup codes for that
  user in `Admin console > Directory > Users`.
- **Suspending a Google account doesn't always end sessions** in other
  services. Say so in the offboarding list, service by service.
- **Stop and ask** if the domain is registered under a person who has
  left, or nobody knows where it is registered. That comes first.
- **Never** ask for, repeat or record a password, a recovery code or a
  2-Step Verification code.

## Evidence

| Check | Record |
|---|---|
| D1 | The registrar's and DNS host's names, the owner address of each, two-step on, transfer lock on, the date, who checked |
| D2 | The number of active users, and that each one matches a person who works there; the names of anyone suspended |
| D3 | Each shared address and the group it now is; any shared account kept until `password-manager`, and why |
| D4 | The 2-Step Verification setting, its allowed methods and its enforcement date; that `Admin console > Reporting > User reports > Security` shows everyone enrolled (the report can lag by up to 48 hours) |
| D5 | Where the inventory is kept, and the number of services on it |
| D6 | For each service on the inventory: `google`, `password` or `other` |
| D7 | The SPF, DKIM and DMARC records as published (they are public), and the date the policy moved to `quarantine` |
| D8 | Where the offboarding list is kept |

## Variants

### Microsoft 365

The same checks apply, with Microsoft's names:

- D2, D3: users and shared mailboxes, or Microsoft 365 groups, in the
  Microsoft 365 admin center.
- D4: turn on security defaults (`Microsoft Entra admin center >
  Entra ID > Overview > Properties > Manage security defaults`). They
  require everyone to register for multi-factor authentication, with
  Microsoft Authenticator or another authenticator app.
- D6: "Sign in with Microsoft" wherever a service offers it.
- D7: DKIM in `Microsoft Defender portal > Email & collaboration >
  Policies & rules > Threat policies > Email authentication settings >
  DKIM`.

Microsoft 365 Business Basic costs $7.00 per person per month, the US
list price since July 1, 2026 (checked 2026-11-12).

## Why this default

- **Google Workspace**, because most small teams already use it, and
  because "Sign in with Google" is on nearly every tool they buy. Moving
  to it from Microsoft 365, or the other way, isn't worth it for this:
  use the variant.
- **Business Starter** covers every check here. Upgrade for storage or
  features, not for this module.
- **2-Step Verification now, keys later.** Phone prompts and
  authenticator apps can be phished, but they stop most attacks on
  reused passwords today. `hardware-keys` finishes the job.
- **Given up:** with one sign-in for everything, the Google account is
  now the key to every door. That is why the next three modules protect
  it: a password manager for its recovery codes, keys for its sign-in,
  and separate admin accounts.

## Sources

All checked 2026-11-12.

- [Google Workspace pricing](https://workspace.google.com/pricing): Business Starter $7 annual, $8.40 flexible; Business Standard $14 and $16.80.
- [Business editions](https://knowledge.workspace.google.com/admin/getting-started/editions/business-editions): at most 300 users.
- [Compare Business editions](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-business-editions): 2-Step Verification, security keys and Google as a SAML identity provider are all in Business Starter.
- [Deploy 2-Step Verification](https://knowledge.workspace.google.com/admin/security/deploy-2-step-verification): enforcement, allowed methods, "Only security key" covers passkeys too.
- [Control which apps access Google Workspace data](https://knowledge.workspace.google.com/admin/apps/control-which-apps-access-google-workspace-data): "Sign in with Google" for third-party apps.
- [Set up DKIM](https://knowledge.workspace.google.com/admin/security/set-up-dkim): `Apps > Google Workspace > Gmail > Authenticate email`, 2048-bit keys.
- [Email sender guidelines](https://support.google.com/a/answer/81126): all senders need SPF or DKIM; senders of more than 5,000 messages a day also need DMARC. This module asks for all three whatever the volume.
- [Microsoft 365 pricing updates, 2026](https://www.microsoft.com/en-us/licensing/news/2026-m365-packaging-pricing-updates): Business Basic $7.00 from July 1, 2026.
- [Security defaults](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults): free in every Microsoft 365 organization, on by default in those created after October 2019.
