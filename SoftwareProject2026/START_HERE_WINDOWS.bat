@echo off
cd /d "%~dp0MillionaireQuiz_Folder"
where py >nul 2>nul
if %errorlevel%==0 (
  py main.py
) else (
  python main.py
)
if errorlevel 1 (
  echo.
  echo The quiz could not start. Check that Python 3.10+ and Tkinter are installed.
  pause
)
