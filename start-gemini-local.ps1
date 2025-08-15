param(
    [string]$ProjectPath
)

Write-Host "`n=== 在本目錄啟動gemini ===" -ForegroundColor Cyan
Set-Location $ProjectPath
Write-Host "📂 已切換到資料夾：$ProjectPath" -ForegroundColor Cyan

Start-Process powershell -ArgumentList "-NoExit -Command `"gemini`""