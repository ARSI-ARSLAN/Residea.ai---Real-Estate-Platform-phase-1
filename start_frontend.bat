@echo off
echo Starting Residea.ai Frontend...
echo.

cd Residea.ai_Frontend

echo Installing dependencies (if needed)...
call npm install

echo.
echo Starting Vite development server...
echo Frontend will be available at: http://localhost:5173
echo.

npm run dev
