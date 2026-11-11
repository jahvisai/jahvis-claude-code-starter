# My Workspace

Updated: <YYYY-MM-DD>

> Template. Replace every <angle-bracket placeholder>, delete departments you will not open
> weekly, delete these > lines. Keep this file under 100 lines. Area names only: no client names
> or prices here, because this file loads into every session below it.

## What this workspace is

<Business name>'s workspace. Everything the business runs lives under this one folder.

## Departments

A department is a folder you start Claude Code in at least weekly.

| Folder | What lives here |
|---|---|
| context/ | shared business brain: overview, offers and pricing, customer personas, brand voice. Read first by every department |
| marketing/ | content, posts, campaigns |
| sales/ | leads, calls, proposals, follow-ups |
| operations/ | SOPs, delivery steps, admin tasks |
| finance/ | invoices, contracts, taxes |
| clients/ | one folder per client, each its own launch point (delete if you have none) |
| inbox/ | anything new that has not been sorted yet |
| archive/ | done or stale work, kept for reference |

## Find your folder

| If you are working on... | Start here |
|---|---|
| a post, a campaign | marketing/ |
| a lead, a quote, a follow-up | sales/ |
| an SOP or a delivery step | operations/ |
| an invoice or taxes | finance/ |
| one client's work | clients/<client>/ |
| who we sell to, what we sell, how we sound | context/ (edit only there) |
| something unsorted | inbox/ |

## Where to start a session

- Start Claude Code in the department (or the one client) the job belongs to.
- Open context/ only to edit it. Open this root only to edit this map.
- Never start in your home folder, Desktop, Documents or Downloads.
- Instructions and skills flow down from this root. Settings do not: each folder you start in
  needs its own `.claude/settings.json`.

## Hard rules

- <the one thing Claude must never do without asking you>
- Never read, print or copy a real key. Keys live in one `.env` per project.
