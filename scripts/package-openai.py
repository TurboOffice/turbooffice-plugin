#!/usr/bin/env python3
"""Export the portable OpenAI package without the Claude marketplace or local files."""

import argparse
import json
import re
import shutil
import zipfile
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("output", type=Path, help="Directory outside this repository for the copy and ZIP")
args = parser.parse_args()
source = Path(__file__).resolve().parents[1]
output = args.output.resolve()
if output == source or source in output.parents:
    parser.error("Output must be outside the plugin repository")
manifest = json.loads((source / "plugin.json").read_text())
name, version = manifest["name"], manifest["version"]
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
    parser.error("Invalid plugin name")
if not re.fullmatch(r"\d+\.\d+\.\d+", version):
    parser.error("Expected a three-part numeric version")
interface = manifest["extensions"]["com.openai"]["interface"]
files = {Path("plugin.json"), Path("mcp.json"), Path("LICENSE")}
files.update(path.relative_to(source) for path in (source / "skills").glob("*/SKILL.md"))
for field in ("logo", "composerIcon", "logoDark", "composerIconDark"):
    if field in interface:
        files.add(Path(interface[field]))
target = output / name
if target.exists():
    parser.error(f"Copy already exists: {target}; choose a fresh output directory")
for relative in files:
    path = source / relative
    if relative.is_absolute() or ".." in relative.parts or path.is_symlink() or not path.is_file():
        parser.error(f"Invalid package file: {relative}")
target.mkdir(parents=True)
for relative in sorted(files):
    destination = target / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source / relative, destination)
archive = output / f"{name}-{version}-openai-draft.zip"
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
    for relative in sorted(files):
        bundle.write(target / relative, str(Path(name) / relative))
with zipfile.ZipFile(archive) as bundle:
    assert bundle.testzip() is None
    assert set(bundle.namelist()) == {str(Path(name) / relative) for relative in files}
print(f"Prepared {archive} ({len(files)} files). This export does not certify submission readiness.")
