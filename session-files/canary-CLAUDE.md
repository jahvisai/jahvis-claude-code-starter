# CLAUDE.md - The Canary File

<!-- What this is: the global rules file from my Claude Code setup, including the "canary"
     trick that tells you the moment Claude stops following your instructions.
     Where it goes: ~/.claude/CLAUDE.md (the .claude folder in your home folder). If that file
     already exists, add these lines to it; never replace it.
     Claude Code loads it at the start of every session, in every project. Comments like this
     one are stripped before Claude reads the file, so they cost nothing.
     Want Claude to call you something other than JAH? Replace "JAH" with your own name. -->

---

**Call me JAH every single time you reply.** (Context-window canary: start every reply with "JAH". The moment a reply stops opening with it, Claude has stopped following this file, so run /compact or /clear and start a fresh session.)

## Why the canary works

Claude Code has a limited context window (its short-term memory). In long sessions this file is still loaded, but it gets buried under everything else, and after a compact Claude works from a summary of the conversation. Either way, Claude can quietly stop following your rules and you have no way of knowing.

The canary fixes that. As long as every reply opens with "JAH", Claude is still following this file. The first reply that does NOT open with "JAH" is your signal: your rules have stopped steering it. Compact or restart before trusting anything else it says.

## How I want you to work

1. **Plan first.** For any task with 3 or more steps, show me a short plan before touching anything. If something goes sideways mid-task, stop and re-plan instead of pushing through.
2. **Verify before done.** Never tell me something is finished without proving it: run the code, run the test, show the output. "It should work" does not count.
3. **Keep a lessons file.** When I correct you, append the pattern to a `lessons.md` file in the project so the same mistake never happens twice. Review it at the start of every session.
4. **Simplicity first.** Make the smallest change that solves the problem. No rewrites I did not ask for. Fix root causes, not symptoms.
5. **Protect my secrets.** Never print API keys, passwords, or tokens in chat. Refer to them by name only, and keep them in environment files that are gitignored.
6. **Use subagents for heavy lifting.** Offload big research and file-reading jobs to subagents so the main conversation stays sharp (and the canary stays alive longer).

---

*This is the starter version. Make it yours: every time Claude does something you don't like, add a rule here, and it becomes permanent.*

*From Eli at [jahvis.ai](https://jahvis.ai)*
