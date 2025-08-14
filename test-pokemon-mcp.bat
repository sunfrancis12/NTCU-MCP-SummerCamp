@echo off
setlocal

REM 專案目錄（根目錄）
set "projectPath=%cd%"

REM 專案資料夾（Pokemon-MCP-Server）
set "targetPath=%projectPath%\Pokemon-MCP-Server"

REM 呼叫 PowerShell 啟動 MCP server
powershell -ExecutionPolicy Bypass -File "%~dp0test-pokemon-mcp.ps1" -ProjectPath "%projectPath%" -TargetPath "%targetPath%"