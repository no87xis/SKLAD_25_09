# 🏢 Sirius Group - Система управления складом

> **Комплексная система управления складом и интернет-магазин для Sirius Group**

## 🎯 Что это такое

Система включает:
- **Админку** для управления товарами, заказами, поставками
- **Интернет-магазин** с корзиной и системой заказов  
- **QR-сканер** для быстрой проверки заказов
- **Систему доставки** с автоматическим расчетом стоимости
- **WhatsApp интеграцию** для связи с менеджерами

## 🚀 Быстрый старт

### Супер-простое развертывание
📖 **[SIMPLE_GUIDE.md](SIMPLE_GUIDE.md)** - для начинающих (2 команды)

### Полное развертывание  
📖 **[DEPLOYMENT.md](DEPLOYMENT.md)** - детальное руководство

### Проблемы с сервером
📖 **[SERVER_GUIDE.md](SERVER_GUIDE.md)** - решение проблем

## ⚡ Быстрое развертывание

```bash
# Linux/Mac (одна команда):
wget https://raw.githubusercontent.com/no87xis/Sirius_sklad_new/master/simple_deploy.sh && chmod +x simple_deploy.sh && ./simple_deploy.sh

# Windows (две команды):
git clone https://github.com/no87xis/Sirius_sklad_new.git && cd Sirius_sklad_new
deploy.bat
```

**Результат:** Рабочий сервер на http://localhost:8000

## 🐧 Production развертывание с systemd

### 1. Создание systemd сервиса
```bash
sudo nano /etc/systemd/system/sirius-sklad.service
```

Содержимое файла:
```ini
[Unit]
Description=Sirius Sklad Web Application
After=network.target

[Service]
Type=exec
User=www-data
Group=www-data
WorkingDirectory=/path/to/sirius_sklad_new
Environment=PATH=/path/to/sirius_sklad_new/venv/bin
Environment=ENVIRONMENT=production
Environment=DEBUG=false
ExecStart=/path/to/sirius_sklad_new/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### 2. Активация сервиса
```bash
sudo systemctl daemon-reload
sudo systemctl enable sirius-sklad
sudo systemctl start sirius-sklad
sudo systemctl status sirius-sklad
```

### 3. Управление сервисом
```bash
# Запуск
sudo systemctl start sirius-sklad

# Остановка
sudo systemctl stop sirius-sklad

# Перезапуск
sudo systemctl restart sirius-sklad

# Просмотр логов
sudo journalctl -u sirius-sklad -f

# Проверка статуса
sudo systemctl status sirius-sklad
```

## 📁 Структура проекта

```
sirius_sklad_new/
├── 📱 app/                 # Основное приложение
│   ├── main.py            # Точка входа FastAPI
│   ├── models/            # SQLAlchemy модели
│   ├── routers/           # API маршруты  
│   ├── services/          # Бизнес-логика
│   ├── templates/         # Jinja2 шаблоны
│   └── static/            # CSS, JS, изображения
├── 📚 doc/                # Техническая документация
├── 📋 docs/               # Спецификации и руководства
├── 🔧 scripts/            # Скрипты управления
├── 🧪 tests/              # Автоматические тесты
├── 🗄️ alembic/           # Миграции БД
└── 📖 README.md           # Эта документация
```

## 🔧 Основные функции

- ✅ Управление товарами (создание, редактирование, удаление)
- ✅ Управление заказами
- ✅ Интернет-магазин с корзиной
- ✅ Система статусов товаров (В наличии, Под заказ, В пути)
- ✅ Загрузка фотографий товаров
- ✅ Аутентификация и авторизация
- ✅ Управление поставками

## 🌐 Доступные страницы

- **Админка:** `http://localhost:8000/` - Управление складом
- **Магазин:** `http://localhost:8000/shop` - Интернет-магазин
- **API:** `http://localhost:8000/docs` - Swagger документация

## 🔐 Стандартные учетные данные

- **Админ:** admin / admin123
- **Менеджер:** manager / manager123

## 📚 Документация

### 📖 Основные руководства
- **[SIMPLE_GUIDE.md](SIMPLE_GUIDE.md)** - Супер-простое развертывание (2 команды)
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Полное руководство по развертыванию  
- **[SERVER_GUIDE.md](SERVER_GUIDE.md)** - Управление сервером и решение проблем
- **[UPGRADE_INSTRUCTIONS.md](UPGRADE_INSTRUCTIONS.md)** - Инструкции по обновлению

### 📋 Техническая документация
- **[doc/](doc/)** - Детальная техническая документация
  - [Обзор проекта](doc/project_overview.md)
  - [API каталог](doc/api_catalog.md) 
  - [Модель данных](doc/data_model.md)
  - [Бизнес-процессы](doc/flows.md)
  - [Конфигурация](doc/config_deploy.md)
- **[docs/](docs/)** - Спецификации и руководства

### 🖥️ Запуск на Windows (через scripts/win)

```cmd
# Сборка проекта
scripts\win\make.bat

# Запуск dev-сервера  
scripts\win\make.bat up

# Проверка статуса
scripts\win\make.bat status

# Остановка сервера
scripts\win\make.bat down
```

### Детальное описание скриптов

#### `scripts/win/make.bat`
- **Назначение:** Универсальный скрипт для управления проектом
- **Команды:**
  - `make.bat` - полная подготовка проекта к работе
  - `make.bat up` - запуск dev-сервера
  - `make.bat down` - остановка сервера
  - `make.bat status` - проверка статуса сервера
  - `make.bat logs` - просмотр логов сервера
- **Что делает:**
  - Проверяет Python и создает виртуальное окружение
  - Устанавливает зависимости из requirements.txt
  - Применяет миграции Alembic
  - Создает папку logs и файл .env
  - Проверяет корректность импорта приложения

#### `scripts/win/serve_dev.cmd`
- **Назначение:** Запуск dev-сервера с автоматическим перезапуском
- **Что делает:**
  - Проверяет виртуальное окружение и зависимости
  - Проверяет, что порт 8000 свободен
  - Запускает uvicorn в отдельном окне
  - Сохраняет PID процесса в logs/uvicorn-dev.pid
  - Записывает логи в logs/uvicorn-dev.log

#### `scripts/win/serve_status.cmd`
- **Назначение:** Проверка статуса сервера и диагностика
- **Что показывает:**
  - Статус PID файла и процесса
  - Занятые порты (netstat)
  - Активные процессы Python
  - Последние 10 строк логов
  - Список файлов в папке logs

#### `scripts/win/serve_stop.cmd`
- **Назначение:** Корректная остановка dev-сервера
- **Что делает:**
  - Читает PID из logs/uvicorn-dev.pid
  - Останавливает процесс через taskkill
  - Удаляет PID файл
  - Проверяет освобождение порта 8000

### Полезные команды

#### Управление сервером через make.bat:
```cmd
scripts\win\make.bat up      # Запуск сервера
scripts\win\make.bat down    # Остановка сервера
scripts\win\make.bat status  # Проверка статуса
scripts\win\make.bat logs    # Просмотр логов
```

#### Просмотр логов в реальном времени:
```powershell
powershell Get-Content logs\uvicorn-dev.log -Wait -Tail 10
```

#### Проверка доступности сервера:
```cmd
curl http://127.0.0.1:8000/
```

#### Принудительная остановка всех Python процессов:
```cmd
taskkill /f /im python.exe
```

### Устранение проблем

#### Сервер не запускается:
1. Проверьте, что порт 8000 свободен: `netstat -an | findstr :8000`
2. Убедитесь, что виртуальное окружение активировано
3. Проверьте логи: `scripts\win\make.bat logs`

#### Сервер завис:
1. Остановите через `scripts\win\make.bat down`
2. Если не помогает: `taskkill /f /im python.exe`
3. Удалите файл `logs\uvicorn-dev.pid` вручную

#### Ошибки зависимостей:
1. Переустановите зависимости: `pip install -r requirements.txt --force-reinstall`
2. Пересоздайте виртуальное окружение: `rmdir /s venv && python -m venv venv`

## 📝 Примечания

- Система использует SQLite для локальной разработки
- Для продакшена рекомендуется PostgreSQL
- Все файлы загружаются в `app/static/uploads/`
- База данных создается автоматически при первом запуске
- Логи сервера сохраняются в папке `logs/`
- PID файлы используются для корректной остановки процессов
