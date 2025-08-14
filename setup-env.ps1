param(
    [string]$ProjectPath,
    [string]$TargetPath
)

Write-Host "`n=== 檢查 uv 虛擬環境 ===" -ForegroundColor Cyan
Set-Location $ProjectPath

if (Test-Path ".venv") {
    Write-Host "✅ 偵測到已有虛擬環境，直接啟動..." -ForegroundColor Green
    . .\.venv\Scripts\Activate.ps1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ 無法啟動現有虛擬環境。" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "📂 未找到虛擬環境，開始初始化 uv..." -ForegroundColor Yellow

    uv init
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ uv init 失敗，請檢查 uv 是否已安裝。" -ForegroundColor Red
        exit 1
    }

    Write-Host "`n=== 建立虛擬環境 ===" -ForegroundColor Cyan
    uv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ uv venv 失敗。" -ForegroundColor Red
        exit 1
    }

    Write-Host "`n=== 啟動虛擬環境 ===" -ForegroundColor Cyan
    . .\.venv\Scripts\Activate.ps1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ 無法啟動虛擬環境。" -ForegroundColor Red
        exit 1
    }
}

Write-Host "`n=== 安裝所需套件 ===" -ForegroundColor Cyan
uv add httpx "mcp[cli]"
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 套件安裝失敗。" -ForegroundColor Red
    exit 1
}

Write-Host "`n✅ 初始化完成！" -ForegroundColor Green
