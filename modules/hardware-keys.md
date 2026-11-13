---
id: hardware-keys
title: Hardware keys
summary: Two security keys per person, and Google sign-in that accepts only a key, admins first.
depends_on: [password-manager]
applies_to: [google-workspace, microsoft-365]
default: YubiKey 5C NFC
fallback: YubiKey 5 NFC, only for a computer with no USB-C port
cost: Two security keys per person
time: 2 hours for the admin; 30 minutes per person
checked: 2026-11-12
---

# Hardware keys

## The attack

A fake sign-in page can pass a password and a phone prompt or an
authenticator code on to the real Google sign-in as fast as a person
types them, while a security key answers only the real site.

## Cost and time

| | Cost | Time |
|---|---|---|
| YubiKey 5C NFC | Two keys per person: one on the keychain, one stored at home | |
| Setup | | 2 hours for the admin, spread over two weeks |
| Per person | | 30 minutes to register both keys in Google, in 1Password for the owners, and anything else that takes them |

If `admin-split` comes next, order two more keys now for its break-glass
account. For the current price, see Yubico's product page (Sources).
Google Workspace Business Starter and 1Password Business already
include security keys, so no seat or plan changes.

## What done looks like

- **D1.** Every person has two YubiKeys, each with a label that says
  which is which (`daily`, `spare`) and nothing about the accounts. The
  daily key is on their keychain. The spare is stored at home, not in
  the laptop bag.
- **D2.** Both keys are registered on every person's Google account,
  and each person has signed in once with each key.
- **D3.** Every Google Workspace admin is under the 2-Step Verification
  method "Only security key", before anyone else.
- **D4.** Every user is under "Only security key", and security codes
  are off unless a named need is written in the checklist. This
  finishes `work-email` D4.
- **D5.** Every 1Password owner has both keys added as two-factor
  authentication on their 1Password account. This finishes
  `password-manager` D4.
- **D6.** Every other 1Password member unlocks 1Password with Google
  (`password-manager` D4), so the keys on their Google account guard
  their vaults too. They add no key in 1Password.
- **D7.** The domain registrar and the DNS host have the keys of each
  person who signs in to them, where they support security keys. Where
  one doesn't, the checklist says so, and two-step stays on an
  authenticator app.
- **D8.** A written lost-key list says what to do when a key, or both,
  is lost. It is kept next to the offboarding list.

## Steps

1. **Agent.** From the `work-email` user list, count the people and
   ask each one what they sign in from: a laptop with USB-C, a phone with
   NFC, and anything older.
   Propose the order: two YubiKey 5C NFC per person, and a YubiKey 5 NFC
   instead for anyone whose computer has no USB-C port. Add two for
   `admin-split` if it comes next. (D1)
2. **Person.** Buy the keys from Yubico or a reseller it lists. When they
   arrive, label each pair `daily` and `spare` and hand them out. (D1)
3. **Person, each one.** Register both keys on your Google account at
   `myaccount.google.com > Security > 2-Step Verification`, in the
   passkeys and security keys section (Google's help page in Sources
   has a direct link). Google may offer to create a
   passkey on the key; either choice counts as a security key. If the key
   asks you to set a PIN, choose one and keep it in your private
   1Password vault. Then sign out, sign in in a private window with the
   daily key, and again with the spare. Put the spare away. (D1, D2)
4. **Agent.** Check, or ask an admin to check, `Admin console > Directory
   > Users > (the person) > Security > Passkeys & security keys` for every
   user. It should list two keys added by that person. The `Reporting >
   User reports > Security` report counts keys too, but it can lag 48
   hours and can count a phone's built-in key, so use the per-user page.
   List anyone not done, admins first. (D2)
5. **Person.** Once every admin shows two keys: in `Admin console >
   Security > Authentication > 2-step verification`, select a group or
   organizational unit that holds only the admins, and set:
   - methods: "Only security key";
   - the backup code grace period: short, a few days;
   - security codes: "Don't allow users to generate security codes".

   Keep a second browser signed in as an admin while you do it. Then each
   admin signs out and back in with a key. (D3)
6. **Person.** A week later, once step 4 shows two keys for every user,
   make the same three settings at the top-level organizational unit, so
   they apply to everyone. Anyone without a key registered can't sign in
   until an admin helps them (the lost-key list), so don't skip the
   check. (D4)
7. **Person.** In 1Password, as an owner: `Policies > Authentication
   policy > Manage`, and check that security keys are allowed. (D5)
8. **Person, each owner.** Add both keys to your 1Password account:
   1Password.com > your name > Manage Account > More Actions > Manage
   Two-Factor Authentication > Add a Security Key. Do it once per key.
   Everyone else unlocks with Google and has nothing to add. (D5, D6)
9. **Agent.** For the registrar and the DNS host on the `work-email`
   inventory, look up on the vendor's own help pages whether it accepts
   security keys (also called WebAuthn, FIDO2 or passkeys), and how many.
   Report the path, or that it doesn't. (D7)
10. **Person.** At each one that does, the people who sign in to it add
    both of their keys, and sign in once with each. Keep the
    authenticator app there as a second method if the service allows
    only one key. Its recovery codes stay in the restricted vault from
    `password-manager` D8. (D7)
11. **Agent.** Draft the lost-key list, using "When a key is lost" under
    Agent instructions. Name, for this team, who can make backup codes
    for whom: any admin for a regular user; only a super admin for
    another admin. (D8)

## Agent instructions

- **Read first.** Steps 1, 4 and 9 are reading. Report what you find
  before proposing the rest.
- **Admins first, then everyone.** Never propose step 6 until step 5
  has run for a week and every user shows two keys. A user with no key
  under "Only security key" is locked out until an admin makes backup
  codes for them.
- **One admin is a single point of failure.** If there is only one
  admin, say so before step 5: if they lose both keys, only Google's own
  account recovery gets the company back, and it asks for proof of the
  domain. Keep their spare key somewhere they can reach in a day.
  `admin-split` adds a second admin and a break-glass account. Do it
  next.
- **Passkeys count.** Google's "Only security key" accepts passkeys as
  well as hardware keys. A person who also saves a passkey on their phone
  or laptop can sign in with it. That is still phishing-resistant, but
  the check is two hardware keys, so record the hardware keys.
- **1Password can't require keys only** for the owners. It asks for the
  second factor only on a new device, and an authenticator app stays
  allowed. Say so; the keys are still worth adding.
- **Services that use Google sign-in need nothing more.** They inherit
  the key through Google. Don't add keys to other services in this
  module; note any that ask.
- **When a key is lost**, the list says:
  1. Sign in with the other key. Remove the lost one from Google (`2-Step
     Verification` settings), 1Password (owners only), the registrar and
     the DNS host.
  2. Order a replacement. Register it everywhere, and make it the new
     spare.
  3. Both keys lost: an admin generates backup codes in `Admin console >
     Directory > Users > (the person) > Security > 2-Step Verification >
     Get backup verification codes`, and gives them to the person on a
     call or in person, after recognizing them. Never on the word of an
     email or a chat message. Members are back in 1Password once they
     can sign in to Google. For an owner, another owner recovers the
     1Password account.
- **Security codes stay off** unless someone must sign in on a machine
  where a key can't reach the browser, such as a remote desktop. Then
  name the need, apply "Allow security codes with remote access" only to
  that person's group, and record it.
- **Never** ask for a key's PIN, a backup code or a recovery code, and
  never hold a key.

## Evidence

| Check | Record |
|---|---|
| D1 | The number of keys handed out, and each person's yes that the spare is stored apart, with the date |
| D2 | For each user: two keys listed on the per-user Security page, and the date |
| D3 | The group or unit name, its 2-Step Verification method, the grace period, the security code setting, the date |
| D4 | The same settings at the top level, and any named exception with the reason and who agreed |
| D5 | For each owner: their yes that both keys are added, with the date |
| D6 | That `password-manager` D4 is done: Unlock with SSO on for everyone but the owners, and the date |
| D7 | For the registrar and the DNS host: keys added and by whom, or "no key support" with the help page checked |
| D8 | Where the lost-key list is kept |

## Variants

### A computer with no USB-C port

Give that person a YubiKey 5 NFC, which plugs into USB-A and taps on a
phone the same way. Everything else is the same.

### Microsoft 365

- D2: enable passkeys in `Microsoft Entra admin center > Entra ID >
  Security > Authentication methods > Policies > Passkey (FIDO2)`, with
  "Allow self-service set up" on. Each person adds both keys at
  `mysignins.microsoft.com/security-info`. Passkeys on keys are in every
  Entra ID edition.
- D3, D4: requiring keys needs Conditional Access with the built-in
  "Phishing-resistant MFA strength". Conditional Access needs Microsoft
  Entra ID P1, which is in Microsoft 365 Business Premium, not in Basic
  or Standard. That is a paid upgrade: give the cost and let the founder
  decide. Without it, register the keys anyway and record D3 and D4 as
  `blocked`, with the reason.
- D5 to D8 are the same.

## Why this default

- **Keys, because they don't get phished.** Phone prompts and codes
  stop most password attacks, but a person can be tricked into passing
  them on. A key checks the site's address itself.
- **YubiKey 5C NFC**, because one key covers USB-C laptops and, by
  tapping, phones. It needs no battery and works with Google, Microsoft
  and 1Password.
- **Two keys per person**, so a lost key is an errand, not a lockout.
- **"Only security key", with security codes off**, because any weaker
  method left on is the one a fake page will ask for.
- **Given up:** a person who forgets their daily key at home waits for an
  admin's backup codes, or goes home. And a team with one admin depends
  on that admin's two keys until `admin-split` is done.

## Sources

All checked 2026-11-12.

- [YubiKey 5C NFC](https://www.yubico.com/product/yubikey-5c-nfc/): current price; USB-C and NFC; FIDO2 and FIDO U2F; no battery.
- [YubiKey 5 NFC](https://www.yubico.com/product/yubikey-5-nfc/): USB-A and NFC.
- [Deploy 2-Step Verification](https://knowledge.workspace.google.com/admin/security/deploy-2-step-verification): `Security > Authentication > 2-step verification`; "Only security key" covers security keys and passkeys; security code options; under "Only security key", only an admin can make backup codes; settings per organizational unit or group.
- [Manage a user's security settings](https://knowledge.workspace.google.com/admin/security/manage-a-users-security-settings): `Directory > Users > Security`, "Passkeys & security keys", "Get backup verification codes"; only super admins make codes for other admins.
- [User reports: Security](https://knowledge.workspace.google.com/admin/reports/user-reports-security): key counts can be inflated by built-in keys, and lag up to 48 hours.
- [Use a security key for 2-Step Verification](https://support.google.com/accounts/answer/6103523): registering, passkey or plain key, removing a lost key.
- [Compare Business editions](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-business-editions): security keys are in Business Starter.
- [Use a security key with 1Password](https://support.1password.com/security-key/): `Manage Account > More Actions > Manage Two-Factor Authentication > Add a Security Key`; more than one key.
- [Manage two-factor authentication](https://support.1password.com/manage-two-factor-authentication/): the Authentication policy; security keys allowed; no setting to require keys only.
- [Cloudflare two-factor authentication](https://developers.cloudflare.com/fundamentals/user-profiles/2fa/): an example of a DNS host and registrar that takes several security keys.
- [Enable passkeys (FIDO2) in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2): the policy path; in every Entra ID edition.
- [Conditional Access authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths): "Phishing-resistant MFA strength"; needs Entra ID P1.
- [Admin account security in Microsoft 365 for business](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-account-security-admins): Business Premium, through Entra ID P1, can require phishing-resistant sign-in.
