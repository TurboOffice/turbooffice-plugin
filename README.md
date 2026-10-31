# TurboOffice for Claude

TurboOffice is the platform real estate brokerages and their agents use to run listings and buyer deals from the
agreement through closing. This plugin connects Claude to it.

With the plugin, Claude can read your deals, offers and their counters and amendments, the documents on file, your
tasks and key dates, and what each deal still needs. It can keep your tasks, appointments and notes, and hand
drafting to TurboOffice's own assistant. Anything that binds or ends a contract or sends paper for signatures waits as a card for your approval.
Starting a listing or preparing its seller disclosure can email the sellers an invitation to complete it.
Signing always happens in TurboOffice.

## What is in it

- `skills/turbooffice/SKILL.md`: when Claude should use TurboOffice, and the same guidance the TurboOffice server
  gives every assistant.
- `skills/<name>/SKILL.md`, one per kind of work, the same catalog TurboOffice's own assistant works from (`offer`,
  `contract`, `sign`, `route-document`, `cma`, `forms`, `signers`, `deal`, `agreement-terms`, `migrate`): what that work needs before it starts and how its tools are used, word for word what the
  server's `load_skill` tool answers for it. A skill whose work runs in TurboOffice's own assistant says so, and
  Claude hands that work over with `work_on`.

Every skill file is generated from the server and never edited by hand.
- `.mcp.json`: the TurboOffice connector, a remote MCP server at `https://turbooffice.ai/mcp`.

## Manifests

`plugin.json` and `mcp.json` at the root are the portable manifests and own every fact the hosts share: name,
version, publisher, links, keywords, icon and the server URL. `scripts/sync-manifests.py` writes
`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.claude-plugin/icon.png`, `.cursor-plugin/plugin.json`
and `.mcp.json` from them;
`--check` fails when one differs, and runs on every push. Edit the root files, then run the script. Each host's
listing description stays in that host's own file.

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

## OpenAI submission preparation

The portable `plugin.json` and `mcp.json` describe the OpenAI package. Its skills are the same generated files
used by Claude. The OpenAI listing includes draft review cases; they are not a record of passed tests.
The publisher is TurboOffice Technologies, Inc.; availability is US-only, with no purchases or payments in the plugin.
The demo recording and portal publisher verification remain incomplete.
Reviewer credentials belong only in the secure submission portal, never in this repository or an archive.

To export a separate upload copy and ZIP, choose a fresh directory outside this repository:

```bash
python3 scripts/package-openai.py /absolute/path/to/submission-output
```

The export includes the portable manifests, generated skills, icon and license. It excludes the Claude marketplace,
compatibility manifests, Git files and preparation scripts. Do not submit the draft until its review materials
and server checks are complete. The monorepo's `docs/mcp/directory-readiness.md` tracks the remaining work.

That export is for OpenAI's submission. Separately, every push to `main` publishes one ZIP with every host's manifests at
its root to `https://assets.turbooffice.ai/downloads/plugin/turbooffice-plugin.zip` (`.github/workflows/publish-zip.yml`),
assuming an AWS role through GitHub's OIDC, so the repository holds no AWS keys.

## Help

- Docs: https://turbooffice.ai/docs
- Support: parker@turbooffice.ai
- Privacy policy: https://turbooffice.ai/privacy
- Terms: https://turbooffice.ai/terms
