---
id: phone-sim
title: Phone and SIM hardening
summary: Each person locks their number at the carrier, sets real PINs, and no account that matters trusts a text message or a phone call.
depends_on: [password-manager]
applies_to: [google-workspace, microsoft-365]
default: The carrier's own number lock and SIM lock
cost: Nothing to buy; these are settings on plans people already have
time: 30 minutes for an admin; 20-30 minutes per person
checked: 2026-11-12
---

# Phone and SIM hardening

## The attack

Someone who talks a carrier into moving a person's number to a new SIM,
or to another carrier, receives every text-message code and reset call
meant for that person, and a default voicemail PIN lets them hear codes
read out by phone.

## Cost and time

| | Cost | Time |
|---|---|---|
| The carrier's locks and PINs | Settings on each person's existing plan | 15-20 minutes per person |
| Voicemail PIN | Included in the plan | 5 minutes per person |
| Removing text and call from the accounts that matter | | 30 minutes for an admin; a few minutes per person per account |

Nothing to buy. Each person's phone and plan stay their own: the company
never sees their PINs, their carrier account or their bill.

## What done looks like

- **D1.** Each person's mobile number has their carrier's number lock
  (it blocks moving the number to another carrier) and SIM lock (it
  blocks moving the number to a new SIM or eSIM) turned on. Where the
  carrier offers neither, the checklist says so.
- **D2.** Each person's carrier account has a PIN or passcode that isn't
  a birthday, an address or digits from the phone number, and a unique
  sign-in password. Both are in the person's private 1Password vault.
- **D3.** Each person's voicemail has a PIN that isn't the default or
  digits from the phone number, kept in their private vault. Voicemail
  doesn't skip the PIN for calls that seem to come from their own phone.
- **D4.** No company Google account can be signed in to or recovered by
  text message or phone call: 2-Step Verification is "Only security
  key" (`hardware-keys` D4), user account recovery is off, super admin
  account recovery is off (`admin-split` D5), and no company account
  has a recovery phone.
- **D5.** The other accounts that matter don't use text messages or
  phone calls for two-step verification or recovery: the domain
  registrar, the DNS host, and every admin or billing login on the
  `work-email` inventory. Where a service requires a phone number, the
  checklist names the service, and that number is locked as in D1.
- **D6.** A written lost-phone list says what to do when a phone is
  lost or stolen, or suddenly shows no service for no clear reason. It
  is kept next to the lost-key list.

## Steps

1. **Agent.** Ask each person which carrier they use, and whether they
   hold the account themselves or are on someone else's plan (a family
   plan, or a company plan). Don't ask for the number. Draft each
   person's steps from the table in step 2. (D1, D2, D3)
2. **Person, each one.** Turn on your carrier's locks, in the carrier's
   app or website:

   | Carrier | Number lock and SIM lock | Who can turn them on |
   |---|---|---|
   | AT&T | Wireless Account Lock: one lock that covers both. In the AT&T app on a phone that is on the account: the person icon, then `Wireless account lock`, then swipe to lock | Anyone with primary or secondary access to the account |
   | Verizon | Number Lock and SIM Protection, two settings, in My Verizon | The account owner, or a manager on the account; check Verizon's current help page |
   | T-Mobile | Port Out Protection (some pages call it Account Takeover Protection) and SIM Protection, in the T-Mobile app or website, line by line | The Primary Account Holder |

   On another carrier, ask it for a lock against number transfers and
   one against SIM changes. On someone else's plan, ask the account
   holder to turn them on for your line. (D1)
3. **Person, each one.** In your carrier account, set the account PIN
   or passcode to random digits that 1Password generates, and change
   the account's sign-in password to a generated one. Save both in your
   private vault. If the carrier offers two-step sign-in with an app,
   use it. (D2)
4. **Person, each one.** Set a voicemail PIN of random digits, in the
   phone's voicemail settings or by calling your voicemail (check your
   carrier's current help page for how). Save it in your private vault.
   If your voicemail lets you skip the PIN when calling from your own
   phone, turn that off: caller ID can be faked. (D3)
5. **Agent.** List the accounts that matter: the company's Google
   accounts, the domain registrar, the DNS host, and every admin or
   billing login on the inventory. For each service, look up on its own
   help pages whether it offers text or call for two-step or recovery,
   and how to remove them. Report the list. (D4, D5)
6. **Person.** A super admin, in `Admin console > Security >
   Authentication > Account recovery > User account recovery`, turns
   off "Allow users and non-super admins to recover their account".
   Users who forget a password or lose both keys ask an admin, as the
   lost-key list says. Check that super admin account recovery is
   still off from `admin-split`. (D4)
7. **Person.** Tell everyone first, then an admin opens `Admin console >
   Directory > Users > (the person) > Security > Recovery information`
   for each user and removes the recovery phone. (D4)
8. **Person, each one.** On each account from step 5 that you sign in
   to, remove text message and phone call as a two-step method and as a
   recovery method. Use your keys, or an authenticator app where keys
   aren't accepted. Where a service won't let you remove the phone (an
   AWS root user, for example, needs its phone number to recover lost
   MFA), leave it, and make sure that number has the D1 locks. (D5)
9. **Agent.** Draft the lost-phone list, using "When a phone is lost"
   under Agent instructions. (D6)

## Agent instructions

- **The phone is the person's own.** Never ask for a PIN, a passcode,
  the carrier account, a bill, a screenshot of the carrier app or the
  phone number. The evidence for D1 to D3 is the person's yes and the
  date.
- **Read first.** Steps 1 and 5 are reading. Report what you find before
  proposing the rest.
- **Locks have to come off to change phones or carriers.** Verizon's
  SIM Protection must be off for a device upgrade. T-Mobile asks for
  Port Out Protection to be off before it gives a transfer PIN. Say so
  when you propose step 2: plan the change, then turn the locks back on.
- **A call asking to turn a lock off is the attack.** AT&T says it will
  never call or text asking you to turn Wireless Account Lock off. Tell
  people to hang up and call the carrier back on the number on its
  website.
- **Don't strand anyone in step 6.** Before user account recovery goes
  off, check that the lost-key list from `hardware-keys` D8 names who
  makes backup codes for whom.
- **When a phone is lost**, the list says:
  1. Call the carrier from another phone to suspend the line, or block
     it in the carrier's app from another device.
  2. Tell an admin, who signs the person out of the company Google
     account's sessions from the user's page in the Admin console. In
     1Password, remove the phone from the account's devices. Check each
     vendor's current help page for where.
  3. Keys still work: sign in elsewhere with a key.
- **No service for no clear reason** can mean the number was moved. The
  list says: call the carrier at once from another phone, then check
  the accounts from step 5 for sign-ins and recovery changes.
- **Stop and ask** if a person isn't the account holder and the holder
  won't turn the locks on. Record D1 `blocked` for that person, with the
  reason.
- **Never** ask for a PIN, a passcode, a one-time code or a password.

## Evidence

| Check | Record |
|---|---|
| D1 | For each person: the carrier, "locks on" or "carrier offers none", their yes, the date |
| D2 | For each person: "PIN and password in my private vault", their yes, the date |
| D3 | For each person: "voicemail PIN set and in my private vault", their yes, the date |
| D4 | The user account recovery setting, the super admin recovery setting, the 2-Step Verification method, and that no user shows a recovery phone, with the date and who checked |
| D5 | For each account on the step 5 list: "no text or call", or the service that requires a phone and that its number is locked |
| D6 | Where the lost-phone list is kept |

## Variants

### A company-paid phone plan

The company is the account holder. An admin sets the number lock and
SIM lock on every line from the business account, and the account's
PIN and sign-in go in the restricted 1Password vault, not a private one.
On Verizon business accounts, only the Primary Contact or an
Administrator can change SIM Protection, and a Verizon representative
can't turn it off. D3 stays each person's own.

### Microsoft 365

- D4: in `Microsoft Entra admin center > Entra ID > Authentication
  methods > Policies`, turn off SMS and Voice call. Then in `Entra ID >
  Password reset > Authentication methods`, turn off Mobile phone and
  Office phone. Microsoft allows a method that is on in any of its
  policies, so both places matter.
- D1 to D3, D5 and D6 are the same.

## Why this default

- **The carrier's own locks**, because the number is held by the
  carrier, not by the person or the company. Only the carrier can
  refuse to move it.
- **Real PINs, kept in the vault**, because a carrier's store and
  support line check the PIN, and a guessable one is no check at all.
- **No text or call on the accounts that matter**, because a code sent
  to a number goes wherever the number goes. Keys from `hardware-keys`
  don't.
- **The person's yes as evidence**, because the phone and plan are
  theirs. The company asks for the setting, never the secret.
- **Given up:** switching phones or carriers takes a planned step to
  turn the locks off and back on, and people who forget a password wait
  for an admin instead of resetting it by text.

## Sources

All checked 2026-11-12.

- [AT&T: Learn about Wireless Account Lock](https://www.att.com/support/article/wireless/000102016): the app steps; who can turn it on.
- [AT&T Wireless Account Lock](https://about.att.com/story/2025/wireless-account-lock.html): what it blocks; AT&T never calls or texts asking to turn it off.
- [Verizon: How does Verizon protect my account](https://www.verizon.com/about/account-security/how-does-verizon-protect-my-account): Number Lock and SIM Protection; SIM Protection off for upgrades.
- [Verizon: Mobile security management](https://www.verizon.com/business/support/account-maintenance-and-management/my-business-wireless-account-management/mobile-security-management): off by default; on business accounts, the Primary Contact or an Administrator; representatives can't turn SIM Protection off.
- [T-Mobile: SIM Protection](https://www.t-mobile.com/support/plans-features/sim-protection) and [Account Takeover Protection](https://support.t-mobile.com/support/plans-features/account-takeover-protection): the names, and the Primary Account Holder.
- [Set up password recovery for users](https://knowledge.workspace.google.com/admin/users/set-up-password-recovery-for-users): `Security > Authentication > Account recovery > User account recovery`.
- [Manage a user's security settings](https://knowledge.workspace.google.com/admin/security/manage-a-users-security-settings): `Directory > Users > Security > Recovery information`; recovery details are used for sign-in challenges.
- [Root user best practices for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html): recovering lost root MFA needs the account's phone number and email.
- [Manage authentication methods in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods-manage): `Authentication methods > Policies`; `Password reset > Authentication methods`; a method on in any policy can be used.
