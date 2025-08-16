@echo off
setlocal

set "projectPath=%cd%"

set "targetPath=%projectPath%\Pokemon-MCP-Server"

powershell -NoExit -ExecutionPolicy Bypass -File "%~dp0install-pokemon-mcp.ps1" -ProjectPath "%projectPath%" -TargetPath "%targetPath%"
