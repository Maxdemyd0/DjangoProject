Write-Host ""
Write-Host "=========================================" -ForegroundColor Blue
Write-Host "      Welcome to the Server Runner"
Write-Host "=========================================" -ForegroundColor Blue
Write-Host ""

Set-Location $PSScriptRoot

$serverIP = Read-Host "Enter IP (default 127.0.0.1)"
$serverPort = Read-Host "Enter Port (default 8000)"

if ([string]::IsNullOrWhiteSpace($serverIP)) { $serverIP = "127.0.0.1" }
if ([string]::IsNullOrWhiteSpace($serverPort)) { $serverPort = "8000" }

Write-Host "Starting server on $serverIP`:$serverPort..."

& ".\.venv\Scripts\python.exe" "manage.py" runserver "$serverIP`:$serverPort"

Write-Host ""
Write-Host "Server stopped." -ForegroundColor Yellow
Read-Host "Press Enter to exit"