@echo off
REM Fitness Chatbot Setup and Run Script for Windows

echo.
echo =========================================
echo Fitness Chatbot - Windows Setup
echo =========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Python version:
python --version
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install dependencies
echo [4/5] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Run the application
echo [5/5] Starting Fitness Chatbot API...
echo.
echo =========================================
echo Fitness Chatbot is starting...
echo =========================================
echo.
echo Server will run at: http://localhost:5000
echo.
echo API Endpoints:
echo   - POST   http://localhost:5000/api/chat
echo   - POST   http://localhost:5000/api/fitness
echo   - POST   http://localhost:5000/api/health
echo   - POST   http://localhost:5000/api/diet
echo   - POST   http://localhost:5000/api/food
echo   - GET    http://localhost:5000/api/greeting
echo   - GET    http://localhost:5000/health
echo.
echo Press Ctrl+C to stop the server
echo.
echo =========================================
echo.

python app.py

pause
