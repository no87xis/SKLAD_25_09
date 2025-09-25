@echo off & chcp 65001 >nul
REM Sirius Group - Перезапуск dev-сервера
REM Интегрированный скрипт для корректного перезапуска

echo.
echo ========================================
echo   Sirius Group - Перезапуск сервера
echo ========================================
echo.

REM Проверяем, что мы в правильной директории
if not exist "app\main.py" (
    echo ОШИБКА: app\main.py не найден. Запустите скрипт из корня проекта.
    pause
    exit /b 1
)

echo 🔄 ПЕРЕЗАПУСК СЕРВЕРА...
echo.

REM 1. Останавливаем сервер через serve_stop.cmd
echo 1. Останавливаем текущий сервер...
call scripts\win\serve_stop.cmd
if %errorlevel% neq 0 (
    echo ⚠️  Предупреждение: Не удалось корректно остановить сервер
)

echo.
echo 2. Ждем завершения процессов...
timeout /t 3 /nobreak >nul

echo.
echo 3. Запускаем новый сервер...
call scripts\win\serve_dev.cmd
if %errorlevel% neq 0 (
    echo ❌ ОШИБКА: Не удалось запустить сервер
    pause
    exit /b 1
)

echo.
echo 4. Проверяем статус...
timeout /t 2 /nobreak >nul
call scripts\win\serve_status.cmd

echo.
echo ✅ ПЕРЕЗАПУСК ЗАВЕРШЕН!
echo 🌐 Сервер доступен: http://127.0.0.1:8000
echo.
