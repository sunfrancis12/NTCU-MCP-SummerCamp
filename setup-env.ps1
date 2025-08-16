#[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

param(
    [string]$ProjectPath,
    [string]$TargetPath
)

Write-Host "`n=== check uv virtual environment ===" -ForegroundColor Cyan
Set-Location $ProjectPath

if (Test-Path ".venv") {
    Write-Host "Found existing virtual environment, activating..." -ForegroundColor Green
    . .\.venv\Scripts\Activate.ps1
    if (-not $env:VIRTUAL_ENV) {
        Write-Host "Failed to activate existing virtual environment." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "Cannot find virtual environment, initializing uv..." -ForegroundColor Yellow

    # If pyproject.toml already exists, skip uv init
    if (Test-Path "pyproject.toml") {
        Write-Host "Found existing pyproject.toml, skipping uv init"
    }
    else {
        uv init
        if ($LASTEXITCODE -ne 0) {
            Write-Host "uv init failed, please check if uv is installed." -ForegroundColor Red
            exit 1
        }
    }

    Write-Host "`n=== create virtual environment ===" -ForegroundColor Cyan
    uv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "uv venv failed." -ForegroundColor Red
        exit 1
    }

    Write-Host "`n=== activate virtual environment ===" -ForegroundColor Cyan
    . .\.venv\Scripts\Activate.ps1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to activate virtual environment." -ForegroundColor Red
        exit 1
    }
}



Write-Host "`n=== install required packages ===" -ForegroundColor Cyan
uv add httpx fastmcp "mcp[cli]"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Package installation failed." -ForegroundColor Red
    exit 1
}

Write-Host "`n=== Initialization complete! ===" -ForegroundColor Green
