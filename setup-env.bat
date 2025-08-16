@echo off
chcp 65001 >nul
setlocal

set "folderName=Pokemon-MCP-Server"

set "repoUrl=https://github.com/sunfrancis12/Pokemon-MCP-Server.git"

set "currentPath=%cd%"

set "targetPath=%currentPath%\%folderName%"

echo.
echo === Pokemon-MCP-Server check and initialize ===
echo.

if exist "%targetPath%" (
    echo  "%folderName%"  found, skipping git clone.
) else (
    echo "%folderName%" not found, starting git clone...
    git clone %repoUrl%
    if %errorlevel% neq 0 (
        echo git clone failed, please check if Git is installed or if there is a network connection.
        pause
        exit /b
    )
)


powershell -ExecutionPolicy Bypass -File "%~dp0setup-env.ps1" -ProjectPath "%currentPath%" -TargetPath "%targetPath%"

pause
