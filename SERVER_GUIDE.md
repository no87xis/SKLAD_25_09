# 🖥️ Руководство по управлению сервером Sirius Group

> **Статус:** KEEP  
> **Назначение:** Комплексное руководство по запуску, настройке и устранению проблем сервера  
> **Кому полезно:** Системным администраторам, DevOps инженерам, разработчикам  
> **Связанные документы:** [DEPLOYMENT.md](DEPLOYMENT.md), [doc/ops_guide.md](doc/ops_guide.md), [doc/runbook_cursor.md](doc/runbook_cursor.md)

## 🚀 Быстрый старт сервера

### Windows (через PowerShell скрипты)
```powershell
# Диагностика и исправление проблем
.\run_diagnosis.ps1

# Запуск сервера
.\start_server.ps1

# Проверка статуса
.\scripts\win\serve_status.cmd

# Остановка сервера
.\scripts\win\serve_stop.cmd
```

### Linux/Mac
```bash
# Активация окружения и запуск
source venv/bin/activate
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

# Запуск в фоне
nohup python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &

# Остановка сервера
pkill -f uvicorn
```

## 🔧 Решенные проблемы сервера

### ✅ Основная проблема: Неактивированное виртуальное окружение

**Симптомы:**
- `ModuleNotFoundError: No module named 'fastapi'`
- Сервер падает при запуске
- Импорты не работают

**Решение:**
```bash
# ВСЕГДА активируйте venv перед работой
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Проверьте активацию
echo $VIRTUAL_ENV  # Linux/Mac
echo %VIRTUAL_ENV%  # Windows

# Должно быть (venv) в начале строки
(venv) PS D:\Sirius_sklad_new>
```

### ✅ Проблемы с PowerShell

**Проблема:** `&&` не работает в PowerShell
```powershell
# ❌ НЕ работает
command1 && command2

# ✅ Работает
command1; command2
```

**Проблема:** Зависания длительных процессов
```powershell
# ❌ НЕ запускайте серверы через run_terminal_cmd
python -m uvicorn app.main:app --reload

# ✅ Используйте готовые скрипты
.\start_server_stable.ps1
scripts\win\serve_dev.cmd
```

### ✅ Проблемы с портами

**Проблема:** Port 8000 already in use
```bash
# Найти процесс на порту
netstat -an | findstr :8000  # Windows
netstat -tlnp | grep :8000   # Linux

# Убить процесс
taskkill /f /im python.exe   # Windows
pkill -f uvicorn             # Linux
```

**Проблема:** Множественные процессы Python
```bash
# Проверить все процессы Python
tasklist | findstr python    # Windows
ps aux | grep python         # Linux

# Убить все процессы Python (ОСТОРОЖНО!)
taskkill /f /im python.exe   # Windows
pkill python                 # Linux
```

## 🛠️ Автоматические инструменты исправления

### 1. Диагностический скрипт `diagnose_and_fix.py`

**Что проверяет:**
- ✅ Активация виртуального окружения
- ✅ Наличие зависимостей
- ✅ Состояние базы данных
- ✅ Импорты приложения
- ✅ Миграции Alembic

**Что исправляет:**
- ✅ Создает .env файл если отсутствует
- ✅ Создает необходимые папки
- ✅ Применяет миграции
- ✅ Проверяет корректность импортов

```python
# Запуск диагностики
python diagnose_and_fix.py
```

### 2. PowerShell скрипты для Windows

#### `run_diagnosis.ps1`
```powershell
# Полная диагностика системы
.\run_diagnosis.ps1
```

**Что делает:**
- Проверяет Python и виртуальное окружение
- Проверяет зависимости
- Тестирует импорты
- Проверяет базу данных
- Запускает `diagnose_and_fix.py`

#### `start_server.ps1`
```powershell
# Запуск сервера с проверками
.\start_server.ps1
```

**Что делает:**
- Активирует виртуальное окружение
- Устанавливает зависимости
- Создает .env файл
- Применяет миграции
- Запускает uvicorn сервер

## 📊 Управление сервисом

### Для systemd (Linux)

#### Создание сервиса
```bash
sudo nano /etc/systemd/system/sirius.service
```

```ini
[Unit]
Description=Sirius Group Warehouse System
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/sirius_sklad_new
Environment=PATH=/path/to/sirius_sklad_new/venv/bin
ExecStart=/path/to/sirius_sklad_new/venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

#### Управление сервисом
```bash
# Активация
sudo systemctl daemon-reload
sudo systemctl enable sirius
sudo systemctl start sirius

# Статус и логи
sudo systemctl status sirius
sudo journalctl -u sirius -f

# Управление
sudo systemctl stop sirius
sudo systemctl restart sirius
```

### Для Windows (через скрипты)

#### Запуск сервера
```cmd
# Основные команды
scripts\win\make.bat up      # Запуск сервера
scripts\win\make.bat down    # Остановка сервера
scripts\win\make.bat status  # Проверка статуса
scripts\win\make.bat logs    # Просмотр логов
```

#### Файлы управления
- `logs\uvicorn-dev.pid` - PID файл процесса
- `logs\uvicorn-dev.log` - основные логи сервера
- `logs\uvicorn-dev.out` - stdout сервера
- `logs\uvicorn-dev.err` - stderr сервера

## 🔍 Диагностика и мониторинг

### Проверка статуса сервера

#### HTTP проверки
```bash
# Основная страница
curl http://localhost:8000/

# Health endpoint
curl http://localhost:8000/health

# API документация
curl http://localhost:8000/docs

# С детальным выводом
curl -v http://localhost:8000/
```

#### Проверка процессов
```bash
# Процессы Python
tasklist | findstr python    # Windows
ps aux | grep python         # Linux

# Процессы uvicorn
tasklist | findstr uvicorn   # Windows
ps aux | grep uvicorn        # Linux

# Занятые порты
netstat -an | findstr :8000  # Windows
netstat -tlnp | grep :8000   # Linux
```

### Логи и отладка

#### Просмотр логов
```bash
# Windows
type logs\uvicorn-dev.log
Get-Content logs\uvicorn-dev.log -Tail 10

# Linux
tail -f server.log
journalctl -u sirius -f
```

#### Уровни логирования
- **INFO** - нормальная работа
- **WARNING** - предупреждения
- **ERROR** - ошибки
- **DEBUG** - отладочная информация

## 🚨 Типичные проблемы и решения

### 1. Сервер не запускается

**Диагностика:**
```bash
# Проверка логов
tail -f server.log

# Проверка порта
netstat -an | findstr :8000

# Проверка виртуального окружения
which python
pip list | grep fastapi
```

**Решения:**
1. Активировать виртуальное окружение
2. Установить зависимости: `pip install -r requirements.txt`
3. Освободить порт 8000
4. Проверить .env файл

### 2. Сервер запускается, но не отвечает

**Диагностика:**
```bash
# Проверка привязки
netstat -an | findstr :8000

# Проверка процесса
ps aux | grep uvicorn
```

**Решения:**
1. Проверить параметр `--host 0.0.0.0`
2. Проверить файрвол
3. Проверить права доступа

### 3. Ошибки импорта модулей

**Диагностика:**
```python
# Проверка импортов
python -c "from app.main import app; print('OK')"
python -c "import fastapi; print('OK')"
```

**Решения:**
1. Активировать venv
2. Переустановить зависимости
3. Проверить PYTHONPATH

### 4. Ошибки базы данных

**Диагностика:**
```bash
# Проверка файла БД
ls -la sirius_sklad.db

# Проверка миграций
alembic current
alembic history
```

**Решения:**
1. Применить миграции: `alembic upgrade head`
2. Проверить права доступа к файлу БД
3. Пересоздать БД при необходимости

### 5. Проблемы с зависимостями

**Диагностика:**
```bash
# Проверка установленных пакетов
pip list
pip check

# Проверка requirements
pip install --dry-run -r requirements.txt
```

**Решения:**
1. Обновить pip: `pip install --upgrade pip`
2. Переустановить зависимости: `pip install -r requirements.txt --force-reinstall`
3. Пересоздать виртуальное окружение

## 💡 Лучшие практики

### Для разработки
1. **ВСЕГДА** активируйте виртуальное окружение
2. **НИКОГДА** не запускайте серверы через Cursor `run_terminal_cmd`
3. Используйте автоматические скрипты
4. Регулярно проверяйте логи
5. Делайте резервные копии БД

### Для продакшена
1. Используйте systemd для автозапуска
2. Настройте мониторинг
3. Ротация логов
4. Регулярные бэкапы
5. Обновления безопасности

### Для отладки
1. Включите DEBUG режим только для разработки
2. Используйте детальные логи
3. Мониторьте производительность
4. Тестируйте на разных окружениях

## 📋 Чек-лист запуска сервера

### Перед запуском:
- [ ] Виртуальное окружение активировано `(venv)`
- [ ] Зависимости установлены `pip list | grep fastapi`
- [ ] .env файл создан и настроен
- [ ] Миграции применены `alembic current`
- [ ] Порт 8000 свободен `netstat -an | findstr :8000`

### После запуска:
- [ ] Сервер отвечает `curl http://localhost:8000/`
- [ ] Нет ошибок в логах
- [ ] API документация доступна `/docs`
- [ ] Health endpoint работает `/health`
- [ ] Процесс записан в PID файл

### При проблемах:
- [ ] Проверить логи сервера
- [ ] Проверить виртуальное окружение
- [ ] Запустить диагностику `python diagnose_and_fix.py`
- [ ] Перезапустить сервер
- [ ] Обратиться к документации

---

> **💡 Источники:** Этот документ объединяет информацию из SERVER_STARTUP_GUIDE.md, SERVER_INSTRUCTIONS.md, SERVER_ISSUES_SOLVED.md  
> **📅 Последнее обновление:** 25 сентября 2025  
> **🔧 Статус:** Все критические проблемы решены
