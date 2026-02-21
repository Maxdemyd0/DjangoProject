Write-Host ""
Write-Host "=========================================" -ForegroundColor Blue
Write-Host "              Migration Tool"
Write-Host "=========================================" -ForegroundColor Blue
Write-Host ""

Set-Location $PSScriptRoot

Write-Host "Running makemigrations..." -ForegroundColor Cyan
& ".\.venv\Scripts\python.exe" manage.py makemigrations

Write-Host ""
Write-Host "Running migrate..." -ForegroundColor Cyan
& ".\.venv\Scripts\python.exe" manage.py migrate

Write-Host ""
Write-Host "Migrations completed." -ForegroundColor Yellow
Read-Host "Press Enter to exit"