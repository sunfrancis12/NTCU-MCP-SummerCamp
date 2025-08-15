@echo off
chcp 65001 >nul
setlocal

REM 要檢查的資料夾名稱
set "folderName=Pokemon-MCP-Server"

REM 要 clone 的 GitHub 連結
set "repoUrl=https://github.com/sunfrancis12/Pokemon-MCP-Server.git"

REM 取得當前目錄
set "currentPath=%cd%"

REM 要檢查的完整路徑
set "targetPath=%currentPath%\%folderName%"

echo.
echo === Pokemon-MCP-Server 檢查與初始化工具 ===
echo.

REM 檢查資料夾是否存在
if exist "%targetPath%" (
    echo ✅ 資料夾 "%folderName%" 已存在，跳過 git clone。
) else (
    echo 📂 找不到 "%folderName%"，開始 git clone...
    git clone %repoUrl%
    if %errorlevel% neq 0 (
        echo ❌ git clone 失敗，請檢查 Git 是否安裝或網路連線。
        pause
        exit /b
    )
)

REM 呼叫 PowerShell 腳本進行 uv 初始化與套件安裝
powershell -ExecutionPolicy Bypass -File "%~dp0setup-env.ps1" -ProjectPath "%currentPath%" -TargetPath "%targetPath%"

pause
