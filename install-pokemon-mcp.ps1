param(
    [string]$ProjectPath,
    [string]$TargetPath
)

Write-Host "`n=== starting virtual environment ===" -ForegroundColor Cyan
if (-Not (Test-Path "$ProjectPath\.venv")) {
    Write-Host "cannot find virtual environment, please run the initialization script first." -ForegroundColor Red
    exit 1
}

# start virtual environment
. "$ProjectPath\.venv\Scripts\Activate.ps1"

$pokeFile = Join-Path $TargetPath "poke.py"
if (-Not (Test-Path $pokeFile)) {
    Write-Host "cannot find $pokeFile" -ForegroundColor Red
    exit 1
}
Write-Host "found poke.py" -ForegroundColor Green

# run uv run fastmcp install mcp-json
Write-Host "`n running uv run fastmcp install mcp-json..." -ForegroundColor Yellow
$uvOutput = uv run fastmcp install mcp-json --server-spec "$pokeFile" | Out-String

# Output to temporary JSON
$tempJsonPath = Join-Path $ProjectPath "mcp_output.json"
$uvOutput | Out-File -Encoding UTF8 $tempJsonPath

# Call Python to process settings.json
Write-Host "`n Updating .gemini/settings.json ..." -ForegroundColor Cyan
python "update-gemini-settings.py" -ProjectPath "$ProjectPath" -McpJson "$tempJsonPath" -PokeFile "$pokeFile"

# Keep the terminal open
Write-Host "`n All done! You can now enter commands." -ForegroundColor Green
powershell
