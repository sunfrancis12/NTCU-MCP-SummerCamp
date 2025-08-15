param(
    [string]$ProjectPath,
    [string]$TargetPath
)

Write-Host "`n=== 啟動虛擬環境 ===" -ForegroundColor Cyan
if (-Not (Test-Path "$ProjectPath\.venv")) {
    Write-Host "❌ 找不到虛擬環境，請先執行初始化腳本。" -ForegroundColor Red
    exit 1
}

# 啟動虛擬環境
. "$ProjectPath\.venv\Scripts\Activate.ps1"

# 確認 Pokemon-MCP-Server/poke.py 是否存在
$pokeFile = Join-Path $TargetPath "poke.py"
if (-Not (Test-Path $pokeFile)) {
    Write-Host "❌ 找不到 $pokeFile" -ForegroundColor Red
    exit 1
}
Write-Host "✅ 找到 poke.py" -ForegroundColor Green

# 執行 uv run fastmcp install mcp-json
Write-Host "`n🚀 執行 uv run fastmcp install mcp-json..." -ForegroundColor Yellow
$uvOutput = uv run fastmcp install mcp-json --server-spec "$pokeFile" | Out-String

# 輸出到臨時 JSON
$tempJsonPath = Join-Path $ProjectPath "mcp_output.json"
$uvOutput | Out-File -Encoding UTF8 $tempJsonPath

# 呼叫 Python 處理 settings.json
Write-Host "`n🐍 更新 .gemini/settings.json ..." -ForegroundColor Cyan
python "update-gemini-settings.py" -ProjectPath "$ProjectPath" -McpJson "$tempJsonPath" -PokeFile "$pokeFile"

# 最後保持終端機，讓使用者可以輸入指令
Write-Host "`n✅ 全部完成！你現在可以輸入指令。" -ForegroundColor Green
powershell
