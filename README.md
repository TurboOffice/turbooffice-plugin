# TurboOffice for Claude

TurboOffice is the platform real estate brokerages and their agents use to run listings and buyer deals from the
agreement through closing. This plugin connects Claude to it.

With the plugin, Claude can read your deals, offers and their counters and amendments, the documents on file, your
tasks and key dates, and what each deal still needs. It can keep your tasks, appointments and notes, and hand
drafting to TurboOffice's own assistant. Anything that binds or ends a contract, sends paper for signatures or emails
people waits as a card for your approval. Signing always happens in TurboOffice.

## What is in it

- `skills/turbooffice/SKILL.md`: when Claude should use TurboOffice, and the same guidance the TurboOffice server
  gives every assistant.
- `skills/<name>/SKILL.md`, one per kind of work, the same catalog TurboOffice's own assistant works from (`offer`,
  `contract`, `sign`, `route-document`, `cma`, `forms`, `signers`, `deal`, `pricing`, `migrate`): what that work needs before it starts and how its tools are used, word for word what the
  server's `load_skill` tool answers for it. A skill whose work runs in TurboOffice's own assistant says so, and
  Claude hands that work over with `work_on`.

Every skill file is generated from the server and never edited by hand.
- `.mcp.json`: the TurboOffice connector, a remote MCP server at `https://turbooffice.ai/mcp`.

## What it runs, sends and fetches

Nothing runs on your computer. Claude calls the TurboOffice server at `https://turbooffice.ai/mcp` after you sign in
with your TurboOffice account and allow access on its consent page (OAuth). TurboOffice receives the requests Claude
sends to its tools. When a request gets stuck, Claude sends the TurboOffice team a short note saying what you wanted,
and tells you it did. TurboOffice does not receive the rest of your conversation.

## Install

In Claude (chat, Cowork or Claude Code), add TurboOffice from the directory, or in Claude Code run:

```
/plugin install turbooffice --marketplace TurboOffice/turbooffice-plugin
```

Then connect the TurboOffice connector and sign in. The steps are at https://turbooffice.ai/docs/connect/claude.

## Requirements

A TurboOffice account at a brokerage that has connecting apps turned on. No account yet? Request access at
https://turbooffice.ai/request-access.

## Help

- Docs: https://turbooffice.ai/docs
- Support: parker@turbooffice.ai
- Privacy policy: https://turbooffice.ai/privacy
- Terms: https://turbooffice.ai/terms
