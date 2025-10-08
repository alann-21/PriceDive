@echo off
REM PriceDive - Run Script for Windows
REM This script runs the PriceDive price tracker

echo ============================================================
echo PriceDive - E-commerce Price Tracker
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

REM Check if config.json exists
if not exist config\config.json (
    echo Error: config\config.json not found!
    echo Please copy config\config.json.example to config\config.json and configure it.
    pause
    exit /b 1
)

REM Run the script
echo Running PriceDive...
echo.
python src\pricedive.py

echo.
echo ============================================================
echo PriceDive execution completed!
echo ============================================================
echo.
echo Generated files:
if exist data\prices.db echo   - data\prices.db (database)
if exist examples\price_trend.png echo   - examples\price_trend.png (chart)
echo.
pause

