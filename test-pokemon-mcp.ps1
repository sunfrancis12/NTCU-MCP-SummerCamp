param(
    [string]$ProjectPath,
    [string]$TargetPath
)

Write-Host "`n=== 啟動 Pokemon-MCP-Server 測試服務 ===" -ForegroundColor Cyan

# 檢查虛擬環境是否存在
if (-Not (Test-Path "$ProjectPath\.venv")) {
    Write-Host "❌ 找不到虛擬環境，請先執行初始化腳本。" -ForegroundColor Red
    exit 1
}

# 啟動虛擬環境
Write-Host "✅ 啟動虛擬環境..." -ForegroundColor Green
. "$ProjectPath\.venv\Scripts\Activate.ps1"

# 切換到專案資料夾
Set-Location $TargetPath
Write-Host "📂 已切換到專案資料夾：$TargetPath" -ForegroundColor Cyan

# 啟動 mcp 測試服務，使用 Start-Process 保持視窗
Write-Host "🚀 啟動 MCP 測試服務..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit -Command `"uv run fastmcp dev poke.py`"" -WorkingDirectory $TargetPath
Write-Host "`n✅ MCP server 已啟動，視窗將保持開啟。" -ForegroundColor Green
