# TurboOffice plugin

TurboOffice is a platform real estate agents and brokerages use to run listings and buyer deals from the agreement
through closing. This plugin connects your AI assistant to your TurboOffice account, so it can read your deals,
documents, tasks and key dates, and help with the work on them. Anything that binds a contract or sends documents
for signatures waits for your approval, and signing happens in TurboOffice.

## What is in it

The plugin is the address of the TurboOffice server (`https://turbooffice.ai/mcp`) and a set of guides: plain
Markdown files that tell your assistant how offers, contracts, signing and documents work in TurboOffice. Nothing runs
on your computer. You sign in with your TurboOffice account through OAuth.

The tools are on the server, so they are current whichever copy of the plugin you have. An older copy keeps working:
its guides may be behind, and your assistant can read the current ones from the server. The Claude, ChatGPT and Cursor
files hold the same guides and differ only in the manifest each assistant reads.

## Connecting

See https://turbooffice.ai/docs for how to connect your assistant.

## Requirements

A TurboOffice account. Request access at https://turbooffice.ai/request-access.

## Help

- Docs: https://turbooffice.ai/docs
- Support: parker@turbooffice.ai
- Privacy: https://turbooffice.ai/privacy
- Terms: https://turbooffice.ai/terms
