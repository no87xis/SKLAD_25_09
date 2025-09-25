# 🚀 Руководство по развертыванию Sirius Group

> **Статус:** KEEP  
> **Назначение:** Единое комплексное руководство по развертыванию системы  
> **Кому полезно:** Разработчикам, DevOps инженерам, системным администраторам  
> **Связанные документы:** [SERVER_GUIDE.md](SERVER_GUIDE.md), [SIMPLE_GUIDE.md](SIMPLE_GUIDE.md), [doc/config_deploy.md](doc/config_deploy.md)

## 📋 Системные требования

### Операционная система
- **Ubuntu 22.04 LTS** (рекомендуется)
- **Windows 10/11** (для разработки)
- **CentOS/RHEL 8+** (альтернатива)

### Программное обеспечение
- **Python 3.8+** (рекомендуется 3.10+)
- **Git** для клонирования репозитория
- **pip** для установки зависимостей
- **curl** для проверки работоспособности
- **nginx** (опционально для проксирования)

## 🚀 Быстрое развертывание

### Linux/Mac
```bash
# 1. Клонируем репозиторий
git clone <your-repo-url>
cd sirius_sklad_new

# 2. Запускаем скрипт развертывания
chmod +x deploy.sh
./deploy.sh

# 3. Запускаем сервер
source venv/bin/activate
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Windows
```cmd
# 1. Клонируем репозиторий
git clone <your-repo-url>
cd sirius_sklad_new

# 2. Запускаем скрипт развертывания
deploy.bat

# 3. Запускаем сервер
venv\Scripts\activate.bat
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 🔧 Детальные шаги установки

### 1. Подготовка системы

#### Ubuntu/Debian:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-venv python3-pip git curl -y
```

#### CentOS/RHEL:
```bash
sudo yum update -y
sudo yum install python3 python3-pip git curl -y
```

#### Windows:
Скачайте и установите Python с [python.org](https://python.org)

### 2. Клонирование и настройка

```bash
# Клонируем репозиторий
git clone <your-repo-url>
cd sirius_sklad_new

# Создаем виртуальное окружение
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate.bat  # Windows

# Устанавливаем зависимости
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Настройка окружения

```bash
# Создаем .env файл
cp .env.example .env

# Редактируем .env (ОБЯЗАТЕЛЬНО измените SECRET_KEY!)
nano .env  # Linux/Mac
# или
notepad .env  # Windows
```

**Основные настройки в .env:**
```env
DATABASE_URL=sqlite:///./sirius_sklad.db
SECRET_KEY=your-super-secure-secret-key-32-chars-minimum
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=False
HOST=0.0.0.0
PORT=8000
UPLOAD_DIR=app/static/uploads
MAX_FILE_SIZE=10485760
```

### 4. Инициализация базы данных

```bash
# Применяем миграции
alembic upgrade head

# Создаем необходимые папки
mkdir -p app/static/uploads
mkdir -p logs
```

### 5. Запуск сервера

#### Режим разработки:
```bash
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

#### Продакшн режим:
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 🐧 Настройка для продакшена

### 1. Создание systemd сервиса

```bash
sudo nano /etc/systemd/system/sirius-sklad.service
```

**Содержимое файла:**
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

### 3. Настройка nginx (опционально)

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/sirius_sklad_new/app/static/;
    }
}
```

## 🔍 Проверка развертывания

### 1. Проверка сервера
```bash
# Проверяем статус
curl http://localhost:8000/

# Проверяем API документацию
curl http://localhost:8000/docs

# Проверяем health endpoint
curl http://localhost:8000/health
```

### 2. Проверка базы данных
```bash
# Проверяем миграции
alembic current
alembic history
```

### 3. Проверка логов
```bash
# Просмотр логов приложения
tail -f logs/app.log

# Проверка systemd логов (если используется)
sudo journalctl -u sirius-sklad -f
```

## 🚨 Устранение проблем

### Сервер не запускается
1. Проверьте, что виртуальное окружение активировано
2. Проверьте, что все зависимости установлены
3. Проверьте .env файл
4. Проверьте логи

### Ошибки базы данных
```bash
# Удалите старую базу данных
rm sirius_sklad.db

# Примените миграции заново
alembic upgrade head
```

### Проблемы с правами доступа
```bash
# Установите правильные права
sudo chown -R www-data:www-data /path/to/sirius_sklad_new
sudo chmod -R 755 /path/to/sirius_sklad_new
```

### Проблемы с портами
```bash
# Проверьте, что порт 8000 свободен
netstat -tlnp | grep 8000

# Убейте процесс, если порт занят
sudo kill -9 $(lsof -ti:8000)
```

## 🎯 Стандартный алгоритм деплоя

### Этап 1: Подготовка (15-30 мин)
1. ✅ Проверка системных требований
2. ✅ Клонирование репозитория
3. ✅ Создание виртуального окружения
4. ✅ Установка зависимостей

### Этап 2: Конфигурация (10-15 мин)
1. ✅ Настройка .env файла
2. ✅ Создание необходимых папок
3. ✅ Применение миграций
4. ✅ Проверка конфигурации

### Этап 3: Запуск (10-20 мин)
1. ✅ Создание systemd сервиса (продакшн)
2. ✅ Запуск сервера
3. ✅ Проверка доступности
4. ✅ Настройка nginx (опционально)

### Этап 4: Проверка (5-10 мин)
1. ✅ Функциональное тестирование
2. ✅ Проверка логов
3. ✅ Проверка производительности
4. ✅ Документирование

**Общее время:** 40-75 минут

## 🔄 Обновление системы

### 1. Остановка сервера
```bash
# Если используете systemd
sudo systemctl stop sirius-sklad

# Или остановите процесс вручную
pkill -f uvicorn
```

### 2. Обновление кода
```bash
# Получаем обновления
git pull origin main

# Обновляем зависимости
pip install -r requirements.txt

# Применяем миграции
alembic upgrade head
```

### 3. Запуск сервера
```bash
# Запускаем заново
sudo systemctl start sirius-sklad
```

## 💾 Резервное копирование

### База данных
```bash
# Создание бэкапа
cp sirius_sklad.db sirius_sklad_backup_$(date +%Y%m%d_%H%M%S).db

# Восстановление
cp sirius_sklad_backup_YYYYMMDD_HHMMSS.db sirius_sklad.db
```

### Загруженные файлы
```bash
# Создание бэкапа
tar -czf uploads_backup_$(date +%Y%m%d_%H%M%S).tar.gz app/static/uploads/

# Восстановление
tar -xzf uploads_backup_YYYYMMDD_HHMMSS.tar.gz
```

## 🎉 Критерии готовности

### ✅ Функциональность (100%)
- Все страницы доступны
- API работает корректно
- База данных инициализирована
- Загрузка файлов работает

### ✅ Производительность
- Время загрузки страниц < 3 сек
- API ответы < 1 сек
- Сервер использует < 512MB RAM

### ✅ Безопасность
- SECRET_KEY изменен
- DEBUG=false в продакшне
- Права доступа настроены
- Файрвол настроен

### ✅ Стабильность
- Сервис автоматически перезапускается
- Логи настроены
- Мониторинг работает
- Нет критических ошибок

## 📞 Поддержка

### Стандартные учетные данные
- **Админ:** admin / admin123
- **Менеджер:** manager / manager123

### Доступные страницы
- **Админка:** `http://your-server-ip:8000/`
- **Магазин:** `http://your-server-ip:8000/shop`
- **API документация:** `http://your-server-ip:8000/docs`

### Важные замечания
1. **Измените SECRET_KEY** в .env файле для продакшена
2. **Настройте файрвол** для доступа к порту 8000
3. **Используйте nginx** для проксирования на порт 80/443
4. **Настройте SSL** для HTTPS в продакшене

---

> **💡 Источники:** Этот документ объединяет информацию из DEPLOYMENT_GUIDE.md, DEPLOYMENT_COMPLETE.md, DEPLOYMENT_FINAL.md, DEPLOY_INSTRUCTIONS.md, DEPLOY_STANDARD.md, GITHUB_DEPLOYMENT.md  
> **📅 Последнее обновление:** 25 сентября 2025  
> **🔧 Статус:** Актуален и готов к использованию