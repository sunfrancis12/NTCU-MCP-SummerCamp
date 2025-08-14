@echo off
setlocal

REM 專案目錄（根目錄）
set "projectPath=%cd%"

REM 呼叫 PowerShell 啟動 MCP server
powershell -ExecutionPolicy Bypass -File "%~dp0start-gemini-local.ps1" -ProjectPath "%projectPath%"
