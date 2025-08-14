import json
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-ProjectPath", required=True)
parser.add_argument("-McpJson", required=True)
parser.add_argument("-PokeFile", required=True)
args = parser.parse_args()

project_path = Path(args.ProjectPath)
mcp_json_path = Path(args.McpJson)
poke_file = Path(args.PokeFile)

# 讀 uv run fastmcp 的 JSON
with open(mcp_json_path, "r", encoding="utf-8-sig") as f:
    mcp_data = json.load(f)

server_names = list(mcp_data.keys())
server_name = server_names[0] if server_names else None
print("get the server name:", server_name)  # poke

# 讀 .gemini/settings.json
gemini_path = project_path / ".gemini" / "settings.json"
gemini_path.parent.mkdir(exist_ok=True)
if gemini_path.exists():
    with open(gemini_path, "r", encoding="utf-8") as f:
        settings = json.load(f)
else:
    settings = {}



# 確認 mcpServers 欄位沒有 poke.py
mcp_server_dict = settings.get("mcpServers", {})
poke_in_dict = any(server_name in str(item.get("serverSpec", "")) for item in mcp_server_dict.values())

if not poke_in_dict:
    mcp_server_dict[server_name] = mcp_data[server_name]
    settings["mcpServers"] = mcp_server_dict
    with open(gemini_path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2, ensure_ascii=False)
    print("✅ 已將 mcp-json 結果插入 .gemini/settings.json")
else:
    print("ℹ️ .gemini/settings.json 已包含 poke.py，跳過更新")
