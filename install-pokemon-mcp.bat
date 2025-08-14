@echo off
setlocal

REM 專案根目錄
set "projectPath=%cd%"

REM 專案資料夾
set "targetPath=%projectPath%\Pokemon-MCP-Server"

REM 呼叫 PowerShell 腳本執行完整流程
powershell -NoExit -ExecutionPolicy Bypass -File "%~dp0install-pokemon-mcp.ps1" -ProjectPath "%projectPath%" -TargetPath "%targetPath%"
