param(
    [string]$ProjectPath
)

Write-Host "`n=== starting gemini ===" -ForegroundColor Cyan
Set-Location $ProjectPath
Write-Host "switch to path: $ProjectPath" -ForegroundColor Cyan

Start-Process powershell -ArgumentList "-NoExit -Command `"gemini`""