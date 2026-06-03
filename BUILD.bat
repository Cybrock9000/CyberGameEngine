@echo off
REM ===== Build Engine with Nuitka =====

python -m nuitka --onefile --windows-disable-console main.py --enable-plugin=tk-inter

echo.
echo Build finished!
pause
