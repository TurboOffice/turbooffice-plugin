#!/usr/bin/env python3
"""Write the Claude and Cursor manifests from the portable plugin.json and mcp.json, or check that they match.

The portable manifests own every fact the hosts share: name, version, publisher, links, keywords, icon and the
server URL. Host-specific copy, such as the Claude listing's description, stays in the host's own file.
"""

import argparse
import json
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--check", action="store_true", help="Exit 1 if a derived file differs; write nothing")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]


def load(relative):
    return json.loads((root / relative).read_text())


def dump(value):
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


manifest = load("plugin.json")
interface = manifest["extensions"]["com.openai"]["interface"]
author = manifest["author"]

claude = load(".claude-plugin/plugin.json")
for key in ("name", "version", "author", "homepage", "repository", "license", "keywords"):
    claude[key] = manifest[key]
claude["privacyPolicyUrl"] = interface["privacyPolicyURL"]

marketplace = load(".claude-plugin/marketplace.json")
marketplace["name"] = manifest["name"]
marketplace["owner"] = {"name": author["name"], "email": author["email"]}
for plugin in marketplace["plugins"]:
    plugin["name"] = manifest["name"]

claude_type = {"streamable-http": "http", "sse": "sse"}
servers = load("mcp.json")["mcpServers"]
claude_mcp = {
    "mcpServers": {
        name: {"type": claude_type[server["type"]], "url": server["url"]} for name, server in servers.items()
    }
}

cursor = {
    "name": manifest["name"],
    "displayName": interface["displayName"],
    **{key: manifest[key] for key in ("version", "description", "author", "homepage", "repository", "license", "keywords")},
    "logo": interface["logo"],
    "mcpServers": "./.mcp.json",
}

derived = {
    Path(".cursor-plugin/plugin.json"): dump(cursor).encode(),
    Path(".claude-plugin/plugin.json"): dump(claude).encode(),
    Path(".claude-plugin/marketplace.json"): dump(marketplace).encode(),
    Path(".mcp.json"): dump(claude_mcp).encode(),
    Path(".claude-plugin/icon.png"): (root / interface["logo"]).read_bytes(),
}

stale = [
    path for path, content in derived.items() if not (root / path).exists() or (root / path).read_bytes() != content
]
if args.check:
    for path in stale:
        print(f"{path} differs from plugin.json/mcp.json; run scripts/sync-manifests.py", file=sys.stderr)
    sys.exit(1 if stale else 0)
for path in stale:
    (root / path).parent.mkdir(exist_ok=True)
    (root / path).write_bytes(derived[path])
    print(f"wrote {path}")
print("Host manifests match plugin.json and mcp.json")
