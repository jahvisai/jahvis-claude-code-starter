---
paths: ["clients/acme/**"]
---

# Acme invoicing rules

- Invoices go out on the 1st, net 15, from the shared billing inbox.
- Always "client," never "customer."
- Never change the tax line on the invoice template.

<!-- How this file works: saved in .claude/rules/, it loads only once Claude opens a file
     that matches the paths: line above (anything under clients/acme/). It never covers a
     command Claude runs or work that doesn't touch those files. A rule that must always
     apply belongs in AGENTS.md, or in a hook if it can never be skipped. -->
