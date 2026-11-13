---
id: admin-audit
title: Least-privilege admin audit
summary: A table of who is admin where, service by service, cut to the fewest people who need each role, and checked every quarter.
depends_on: [admin-split]
applies_to: [google-workspace, microsoft-365]
default: The admin roles each service already has; Google Workspace prebuilt and custom admin roles
cost: Nothing to buy, unless a smaller Google role needs a new admin account (one more Workspace seat each)
time: 2-3 hours for an admin, with the agent; 30 minutes each quarter
checked: 2026-11-12
---

# Least-privilege admin audit

## The attack

Admin rights pile up as a company grows, so a phished account or a
departed person often still holds owner rights in the code host, the
chat workspace, the cloud account or the payment tool, and from there
can add users, read everything or move money.

## Cost and time

| | Cost | Time |
|---|---|---|
| The first audit | | 2-3 hours for an admin, with the agent |
| A smaller Google role on a new admin account | One more Workspace seat per admin account (as in `admin-split`) | 30 minutes |
| Each quarter | | 30 minutes to re-check the table |

Most of the work is reading role lists and removing rights nobody uses.
Nothing is bought unless step 2 adds an admin account. For the current
seat price, see Google's pricing page (Sources).

## What done looks like

- **D1.** An admin table exists, next to the `work-email` service
  inventory. For every service on the inventory that has admin or owner
  roles, it lists each role, who holds it, on which account, and the task
  that needs it. It is built from each service's own role list, not from
  memory.
- **D2.** In Google Workspace, every admin role is on an admin account
  (`admin-split` D4). Super Admin is held only by the admin accounts of
  the people named in `admin-split` D2 and by the break-glass account.
  Any other admin account has the smallest prebuilt or custom role that
  covers its tasks.
- **D3.** In every other service on the table (for example the code
  host, the chat workspace, the cloud account, the billing or payment
  tool, the domain registrar and the DNS host), the role list matches
  the table: the top role is held by at least two people where the
  service allows it, by nobody beyond a written need, and by nobody who
  has left.
- **D4.** Each service's top-level account, the one that can't be
  removed (the cloud account's root user, the payment tool's account
  owner, the chat workspace's primary owner), is on a company address
  or held by a named long-term person. A shared top-level login has its
  password in the restricted 1Password vault (`password-manager` D6).
  The cloud root user has no access keys.
- **D5.** Every admin in a service that doesn't sign in through Google
  has two-step verification on there, with their two keys from
  `hardware-keys` where the service accepts security keys.
- **D6.** Every non-person admin (a bot, an integration, a token, or a
  cloud user with access keys) that holds admin rights is in the table
  with an owner and a reason. Any not used in the last 90 days is
  removed.
- **D7.** The offboarding list says, for each service on the table, how
  to remove a person's admin role and who does it.
- **D8.** The table is re-checked each quarter, and the checklist has
  the date of the last review and the cuts it made.

## Steps

1. **Agent.** From the `work-email` inventory, list every service that
   has admin or owner roles. For each one, ask a person who administers
   it to share the role list as an export or a screenshot showing names
   and roles only. Step 3 says where each list is. (D1)
2. **Agent.** For Google Workspace, ask a super admin for `Admin console
   > Account > Admin roles`: each role and its admins. Check it against
   `admin-split` D4. For each admin account that isn't one of the named
   super admins or the break-glass account, propose the smallest role
   that covers its tasks:
   - User Management Admin for someone who creates, renames and suspends
     users (it can't change admin accounts);
   - Help Desk Admin for someone who only resets passwords;
   - Groups Admin for someone who manages groups;
   - a custom role, made in `Admin console > Account > Admin roles >
     Create new role`, when no prebuilt role fits.

   A daily account that needs a role gets an admin account first, as in
   `admin-split`. Give the seat cost. (D1, D2)
3. **Agent.** For the other services, ask for the list where it lives:
   - **Code host (GitHub):** the organization's `People` tab, with the
     `Role` menu set to `Owner`. Note billing managers, security
     managers and outside collaborators too.
   - **Chat workspace (Slack):** `Directories > People > Filters >
     Account type`, once for owners and once for admins. A workspace
     has one Primary Owner.
   - **Cloud account (AWS):** the IAM console's `Credential report`,
     which lists every IAM user with its MFA status and when its
     access keys were last used, and who holds an administrator policy
     or permission set. For another cloud, the same questions; check
     the vendor's current help page for where.
   - **Billing or payment tool (Stripe):** the team list in its
     settings, with each person's role. Stripe has one Account owner,
     and Super Administrator, Administrator and IAM Administrator roles
     that can all invite users.
   - **Domain registrar and DNS host:** the users or members of each
     account, with their roles.
   - **Anything else on the inventory:** its members page, filtered to
     admins or owners. (D1, D3)
4. **Agent.** Build the table and propose a cut for every row: keep,
   move to a smaller role, or remove, each with a reason. Use the rules
   under Agent instructions. Show it for a yes. (D1, D3)
5. **Person.** For each top-level account: move it onto a company
   address or a named long-term person where it isn't. For the cloud
   root user, follow the provider's own advice: a group email address,
   a long generated password in the restricted vault, MFA with security
   keys (AWS takes up to eight devices, so two people's keys fit), no
   access keys, and daily work through named users or roles instead.
   (D4)
6. **Person.** Make the cuts, one service at a time, signed in as an
   admin who stays. Before lowering or removing anyone, check that at
   least two people who keep the top role can sign in. Lower your own
   role last, if at all. (D2, D3)
7. **Person, each owner (every admin on the table).** In each service
   where you hold admin and sign in with that service's own password,
   turn on two-step verification, add both of your keys if it takes
   them, and an authenticator app if it doesn't. Its recovery codes go in your
   private vault, or the restricted vault for a shared login
   (`password-manager` D8). (D5)
8. **Agent.** From the same lists, list every non-person admin: bots,
   integrations, tokens and cloud users with access keys that hold
   admin rights. For each, record the owner, the purpose and when it
   was last used, where the list shows it (the AWS credential report
   does). Propose removing the unused and narrowing the rest. AI tools
   and agents are for `ai-connector-scopes`; note them there. (D6)
9. **Person.** Remove or narrow them. Where a token is in use, make the
   narrower one first, switch the tool over, then delete the old one.
   (D6)
10. **Agent.** Update the offboarding list: for each service on the
    table, how to remove a person's admin role, and who does it. Update
    the inventory's "who is admin" column from the table. (D7)
11. **Agent.** Each quarter, on the same day as the `admin-split`
    break-glass test, ask for fresh role lists, compare them with the
    table, and propose cuts. (D8)
12. **Person.** Make the cuts, and record the date in the checklist.
    (D8)

## Agent instructions

- **Read first.** Steps 1 to 4 are reading and drafting. Report the
  table before proposing any change.
- **You hold no admin role** and need none here. Work from the lists
  people share. Ask for names and roles only. If a list reaches you with
  a token or key in it, don't repeat it: say it was exposed and should
  be replaced.
- **The rules for a cut:**
  - a need is a task, not a title: "pays the invoices", not "founder";
  - the top role in each service: at least two people where the service
    allows, and rarely more than three in a team this size;
  - the smallest role that covers the task: a billing role for billing,
    a developer role for building, a read-only role for reports;
  - nobody who has left, and no shared login with admin rights except
    a top-level account held in the restricted vault;
  - a role given through a group or team counts as held by each member.
- **Never leave a service without a working top role.** Some roles
  can't be removed, only handed on: Slack's Primary Owner and Stripe's
  Account owner transfer ownership instead. If a cut would leave fewer
  than two people who can sign in with the top role, or one where the
  service allows only one, stop.
- **Optional services stay optional.** If the team has no code host or
  no cloud account, there is nothing to check there. Don't suggest
  adopting one.
- **Stop and ask** if nobody can sign in to a top-level account, or it
  sits under a person who has left. Getting it back comes before any
  cut.
- **Never** change a role yourself, even if a tool gives you access,
  and never ask for a password, a token, a key or a recovery code.

## Evidence

| Check | Record |
|---|---|
| D1 | Where the table is kept, the number of services and roles in it, and the date each list was read |
| D2 | The `Account > Admin roles` list: each role and the admin accounts holding it, and the date |
| D3 | For each service: the role holders after the cuts, that they match the table, and the date |
| D4 | For each top-level account: its address or holder, "password in the restricted vault" where shared, who confirmed; for the cloud root user, MFA devices registered and no access keys, from the credential report |
| D5 | For each admin and each such service: two-step on, keys or app, from their yes and the date |
| D6 | Each non-person admin: owner, purpose, last used; the ones removed, and the date |
| D7 | Where the offboarding list is kept, and the date it was updated |
| D8 | The date of each review, who did it, and the cuts made |

## Variants

### Microsoft 365

- D2: the roles are in `Microsoft Entra admin center > Entra ID > Roles
  & admins > All roles`. Microsoft advises fewer than five Global
  Administrators, plus its two emergency access accounts from
  `admin-split`. For everyone else, pick from Microsoft's "least
  privileged role by task" list.
- D8: Microsoft's own access reviews and just-in-time roles (Privileged
  Identity Management) need Microsoft Entra ID P2 or Entra ID
  Governance, a paid upgrade beyond Business Premium. Without them, the
  quarterly review is done by hand, as above.
- D1, D3 to D7 are the same.

## Why this default

- **Use what each service already has.** Every common tool has roles.
  The work is reading them and cutting, not buying an access tool.
- **Two people, then stop.** Google advises at least two super admins.
  GitHub says owners should be limited "to no less than two people".
  Two keeps the company in when one is away; more is more doors.
- **The agent builds the table, a person cuts.** Reading role lists is
  slow and suits an agent. Removing a role can lock someone out, so a
  person does it.
- **No separate admin accounts outside Google.** Most other services
  give each person one account, and many sign in through Google, which
  `admin-split` already guards. Elsewhere, fewer admins with keys does
  the job.
- **Given up:** people who used to fix things themselves now ask an
  admin, and the quarterly review is a recurring half hour.

## Sources

All checked 2026-11-12.

- [Google Workspace pricing](https://workspace.google.com/pricing): current seat prices.
- [Prebuilt administrator roles](https://knowledge.workspace.google.com/admin/users/prebuilt-administrator-roles): Super Admin, User Management Admin (can't change admin accounts), Help Desk Admin, Groups Admin, Services Admin; at least two super admins.
- [Create, edit, and delete custom admin roles](https://knowledge.workspace.google.com/admin/users/create-edit-and-delete-custom-admin-roles): `Account > Admin roles > Create new role`; super admins only; a custom role can never change an admin account.
- [Roles in an organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization): owner, member, billing manager, security manager; owners "no less than two people".
- [Viewing people's roles in an organization](https://docs.github.com/en/account-and-profile/how-tos/organization-membership/viewing-peoples-roles-in-an-organization): `People`, then the `Role` menu.
- [Types of roles in Slack](https://slack.com/help/articles/360018112273-Types-of-roles-in-Slack): one Primary Owner; Workspace Owners and Admins.
- [Browse people and user groups in Slack](https://slack.com/help/articles/360003534892-Browse-people-and-user-groups-in-Slack): `Directories > People > Filters > Account type`.
- [Root user best practices for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html): use it rarely; up to eight MFA devices, FIDO keys included; no root access keys; a group email address; don't store the password only in tools that depend on the same account.
- [Generate credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html): IAM console, `Credential report`; MFA status and access key last used.
- [Stripe user roles](https://docs.stripe.com/get-started/account/teams/roles): one Account owner; Super Administrator, Administrator and IAM Administrator can invite users.
- [Best practices for Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices): `Entra ID > Roles & admins > All roles`; fewer than five Global Administrators; PIM needs P2 or ID Governance; access reviews.
