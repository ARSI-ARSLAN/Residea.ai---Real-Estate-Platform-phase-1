@echo off
echo Starting Residea.ai Backend Server...
echo.
echo ML Models Directory: Models Trained
echo.

cd Residea.ai_Frontend\backend

echo Checking Django configuration...
python manage.py check
if %errorlevel% neq 0 (
    echo Error: Django configuration check failed!
    pause
    exit /b %errorlevel%
)

echo.
echo Starting Django development server on http://localhost:8000
echo.
echo API Endpoints:
echo - Health Check: http://localhost:8000/api/ml/health/
echo - Properties: http://localhost:8000/api/properties/
echo - Recommendations: http://localhost:8000/api/properties/recommendations/
echo - Admin: http://localhost:8000/admin/
echo.

python manage.py runserver
