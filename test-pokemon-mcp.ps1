param(
    [string]$ProjectPath,
    [string]$TargetPath
)

Write-Host "`n=== starting Pokemon-MCP-Server test service ===" -ForegroundColor Cyan

# Check if virtual environment exists
if (-Not (Test-Path "$ProjectPath\.venv")) {
    Write-Host "Cannot find virtual environment, please run the initialization script first." -ForegroundColor Red
    exit 1
}

# Activate virtual environment
Write-Host "Starting virtual environment..." -ForegroundColor Green
. "$ProjectPath\.venv\Scripts\Activate.ps1"

# Start MCP test service, use Start-Process to keep the window open
Write-Host "Starting MCP test service..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit -Command `"uv run fastmcp dev Pokemon-MCP-Server/poke.py`""
Write-Host "`nMCP server has been started, the window will remain open." -ForegroundColor Green
