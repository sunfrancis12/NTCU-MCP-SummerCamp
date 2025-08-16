@echo off
setlocal

set "projectPath=%cd%"

set "targetPath=%projectPath%\Pokemon-MCP-Server"

powershell -ExecutionPolicy Bypass -File "%~dp0test-pokemon-mcp.ps1" -ProjectPath "%projectPath%" -TargetPath "%targetPath%"