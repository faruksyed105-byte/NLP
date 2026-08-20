@echo off
setlocal
title LexiNLP - Localhost Server

echo =====================================================================
echo   LexiNLP Platform - Starting Localhost Server
echo =====================================================================
echo.

:: Detect Python executable
where python >nul 2>nul
if %errorlevel% equ 0 (
    set PY_CMD=python
    goto RUN
)

where py >nul 2>nul
if %errorlevel% equ 0 (
    set PY_CMD=py
    goto RUN
)

echo [ERROR] Python was not found in your system PATH!
echo Please install Python 3.10+ from https://www.python.org/
echo and make sure to check "Add Python to PATH" during installation.
echo.
pause
exit /b 1

:RUN
echo Starting LexiNLP on http://localhost:8000 ...
echo.
%PY_CMD% run.py --host 127.0.0.1 --port 8000
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Server exited with error code %errorlevel%.
    echo If port 8000 is occupied, you can run: %PY_CMD% run.py --port 8001
    pause
)
