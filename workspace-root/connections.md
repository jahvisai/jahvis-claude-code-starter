# Connections

Updated: <YYYY-MM-DD>

One row per area of the business: the tool you use for it and how Claude reaches that tool.
Claude reads this before it says "I can't see your calendar" or guesses which app holds
your leads.

| Business area | Tool you use | How Claude reaches it | Read only, or read and write | Last tested (date, what you asked) |
|---|---|---|---|---|
| Email | <tool> | not connected yet | | |
| Calendar | <tool> | not connected yet | | |
| Files and documents | <tool> | not connected yet | | |
| Leads and customers | <tool> | not connected yet | | |
| Invoices and payments | <tool> | not connected yet | | |
| Content and social posts | <tool> | not connected yet | | |
| Meetings and call notes | <tool> | not connected yet | | |
| Team chat | <tool> | not connected yet | | |

## How to fill the "How Claude reaches it" column

Write one of these, plus the name Claude Code shows for it:

- `connector`: turned on in the Claude app's connector list
- `MCP server`: added to this workspace's `.mcp.json`
- `command line tool`: a program Claude runs in the terminal
- `exported file`: you download a file and drop it in `inbox/`
- `not connected yet`: Claude cannot reach it

## Rules

- A row counts as connected only after a test. Ask Claude one real question that needs the
  tool, then write the date and the question in the last column.
- Start every new connection as read only. Change it to read and write after a week of
  correct answers.
- Tool names only. No password, key or login ever goes in this file.
- Delete the rows for areas you do not have. Add a row when a new area becomes weekly work.
