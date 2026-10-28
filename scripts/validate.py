#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MCP_URL = "https://tools.service.re8ch.com/tenant/mcp"


def load(name: str) -> dict:
    return json.loads((ROOT / name).read_text())


plugin = load("plugin.json")
mcp = load("mcp.json")
gemini = load("gemini-extension.json")

assert plugin["name"] == "re8ch"
assert plugin["logo"] == "assets/logo.svg"
assert (ROOT / plugin["logo"]).is_file()
assert mcp["mcpServers"]["re8ch"] == {
    "type": "streamable-http",
    "url": MCP_URL,
}
assert gemini["name"] == "re8ch-plugin"
assert gemini["contextFileName"] == "GEMINI.md"
assert gemini["mcpServers"]["re8ch"]["httpUrl"] == MCP_URL
assert (ROOT / "GEMINI.md").is_file()
assert (ROOT / "skills/re8ch/SKILL.md").is_file()

print("Re8ch Cursor and Gemini distribution manifests are consistent")
