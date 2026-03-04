@echo off
echo Starting Auto-Commit System...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH!
    echo Please install Python from python.org
    pause
    exit /b 1
)

REM Install requirements if needed
echo Installing requirements...
pip install -r requirements.txt

echo.
echo Running main script...
python main.py

pause