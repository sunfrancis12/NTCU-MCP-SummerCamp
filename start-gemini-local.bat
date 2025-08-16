@echo off
setlocal

set "projectPath=%cd%"

powershell -ExecutionPolicy Bypass -File "%~dp0start-gemini-local.ps1" -ProjectPath "%projectPath%"
