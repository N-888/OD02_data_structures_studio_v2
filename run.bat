@echo off
REM Переходим в папку, где лежит bat-файл.
cd /d "%~dp0"

REM Сначала пробуем запуск через python.
python main.py 2>nul

REM Если первая команда не сработала, пробуем запуск через py.
if errorlevel 1 py main.py

REM Оставляем окно открытым после завершения.
pause