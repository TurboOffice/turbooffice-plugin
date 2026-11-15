# TurboOffice plugin

TurboOffice is a platform real estate agents and brokerages use to run listings and buyer deals from the agreement
through closing. This plugin connects your AI assistant to your TurboOffice account, so it can read your deals,
documents, tasks and key dates, and help with the work on them. Anything that binds a contract or sends documents
for signatures waits for your approval, and signing happens in TurboOffice.

## How it is organized

- `skills/` holds the guides: one Markdown file for each kind of work (`offer`, `contract`, `sign`, `route-document`,
  `cma`, `forms`, `signers`, `deal`, `agreement-terms`, `migrate`) and `turbooffice`, the overview. They are generated
  from the server and say how its tools are used.
- `mcp.json` (`.mcp.json` for Claude and Cursor) names the server, `https://turbooffice.ai/mcp`. The tools are on the
  server, not in the plugin. Sign-in is OAuth with a TurboOffice account.
- `plugin.json`, `.claude-plugin/` and `.cursor-plugin/` are the manifests, one for each kind of host. The Claude,
  ChatGPT and Cursor packages hold the same skills and differ only in the manifest.
- `assets/` holds the icon. Nothing in the plugin runs.

## Versions

There is one server. Each plugin version is generated from the server as it was at that release, and states its
version in its manifest and in the description of the `turbooffice` skill. The server reports the current version and
each package's download (`whoami`). An older copy still works with the server; its guides describe the tools as
they were at that version, and `load_skill` returns the current guides.

## Connecting

See https://turbooffice.ai/docs for how to connect your assistant.

## Requirements

A TurboOffice account. Request access at https://turbooffice.ai/request-access.

## Help

- Docs: https://turbooffice.ai/docs
- Support: parker@turbooffice.ai
- Privacy: https://turbooffice.ai/privacy
- Terms: https://turbooffice.ai/terms
