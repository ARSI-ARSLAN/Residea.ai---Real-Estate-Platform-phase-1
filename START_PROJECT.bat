@echo off
echo ========================================
echo   Residea.ai - ML-Powered Property Recommendations
echo ========================================
echo.
echo This will start both Backend and Frontend servers
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo.
echo Press Ctrl+C in each window to stop the servers
echo.
pause

start "Residea.ai Backend" cmd /k "cd /d %~dp0 && start_backend.bat"
timeout /t 5 /nobreak >nul
start "Residea.ai Frontend" cmd /k "cd /d %~dp0 && start_frontend.bat"

echo.
echo Both servers are starting in separate windows...
echo.
