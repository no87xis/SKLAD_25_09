# 🎯 Простое руководство по Sirius Group

> **Статус:** KEEP  
> **Назначение:** Упрощенные инструкции для быстрого развертывания  
> **Кому полезно:** Начинающим разработчикам, быстрому тестированию  
> **Связанные документы:** [DEPLOYMENT.md](DEPLOYMENT.md), [SERVER_GUIDE.md](SERVER_GUIDE.md)

## 🎯 Что мы делаем
**Берем рабочий код и запускаем на сервере БЕЗ ИЗМЕНЕНИЙ**

## ✅ Что работает у вас локально
- `app/main.py` - импортируется без ошибок
- Все роутеры подключены
- База данных создается
- Сервер запускается

## 🚀 Супер-быстрый старт (2 команды)

### Linux/Mac сервер:
```bash
# 1. Загрузить и запустить скрипт
wget https://raw.githubusercontent.com/no87xis/Sirius_sklad_new/master/simple_deploy.sh
chmod +x simple_deploy.sh && ./simple_deploy.sh
```

### Windows сервер:
```cmd
# 1. Клонировать репозиторий
git clone https://github.com/no87xis/Sirius_sklad_new.git
cd Sirius_sklad_new

# 2. Запустить автоматическое развертывание
deploy.bat
```

## 🔍 Что делает скрипт

### Автоматические шаги:
1. **Останавливает процессы** на сервере
2. **Очищает** старую папку (если есть)
3. **Загружает код** с GitHub
4. **Создает виртуальное окружение**
5. **Устанавливает зависимости**
6. **Создает .env файл**
7. **Создает директории** для загрузок
8. **Инициализирует базу данных** - создает таблицы и админа
9. **Запускает сервер** с ВАШИМ рабочим main.py
10. **Проверяет статус**

### Результат:
✅ Сервер работает на http://your-server-ip:8000  
✅ Админ: admin/admin123  
✅ Все функции работают  

## 🔧 Если нужно развернуть с нуля

### Быстрое развертывание (с потерей данных):
```bash
# 1. Остановите старый сервер
pkill -f uvicorn

# 2. Удалите старую папку
rm -rf sirius_sklad_new

# 3. Клонируйте заново
git clone https://github.com/no87xis/Sirius_sklad_new.git
cd sirius_sklad_new

# 4. Запустите развертывание
./simple_deploy.sh  # Linux/Mac
# или
deploy.bat   # Windows

# 5. Запустите сервер
source venv/bin/activate
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 🎯 Результат развертывания

### ✅ Что получите:
- **Рабочий сервер** на порту 8000
- **Админку** для управления складом
- **Магазин** для клиентов
- **API документацию** на `/docs`

### 🌐 Доступные страницы:
- **Админка:** `http://your-server-ip:8000/`
- **Магазин:** `http://your-server-ip:8000/shop`
- **API:** `http://your-server-ip:8000/docs`

### 🔐 Учетные данные:
- **Админ:** admin / admin123
- **Менеджер:** manager / manager123

## 💡 Ключевая идея
**Мы не исправляем код - мы просто разворачиваем то, что уже работает!**

Никаких сложных настроек, никаких изменений в коде - просто берем рабочую версию и запускаем.

## 📋 Если что-то пошло не так

### Быстрая диагностика:
```bash
# Проверить лог сервера
tail -f server.log

# Проверить статус процессов
ps aux | grep uvicorn

# Проверить порт
netstat -tlnp | grep 8000

# Проверить доступность
curl http://localhost:8000/
```

### Частые проблемы:

| Проблема | Решение |
|----------|---------|
| Порт 8000 занят | `pkill -f uvicorn` |
| Python не найден | Установить Python 3.8+ |
| Модули не найдены | Активировать venv: `source venv/bin/activate` |
| База данных заблокирована | Перезапустить сервер |

### Если ничего не помогает:
```bash
# Полная переустановка (ОСТОРОЖНО - потеря данных!)
rm -rf sirius_sklad_new
git clone https://github.com/no87xis/Sirius_sklad_new.git
cd sirius_sklad_new
./simple_deploy.sh
```

## 🚀 Для более сложных случаев

Если простое развертывание не подходит:

1. **Полное руководство:** [DEPLOYMENT.md](DEPLOYMENT.md)
2. **Проблемы с сервером:** [SERVER_GUIDE.md](SERVER_GUIDE.md)
3. **Техническая документация:** [doc/](doc/)

## ⚡ TL;DR - Очень кратко

```bash
# Все в одной команде (Linux/Mac):
wget https://raw.githubusercontent.com/no87xis/Sirius_sklad_new/master/simple_deploy.sh && chmod +x simple_deploy.sh && ./simple_deploy.sh
```

```cmd
REM Все в двух командах (Windows):
git clone https://github.com/no87xis/Sirius_sklad_new.git && cd Sirius_sklad_new
deploy.bat
```

**Результат:** Рабочий сервер на http://localhost:8000 с админкой и магазином.

---

> **💡 Источники:** Этот документ объединяет информацию из SIMPLE_DEPLOY_INSTRUCTIONS.md, SIMPLE_INSTRUCTIONS.md  
> **📅 Последнее обновление:** 25 сентября 2025  
> **🎯 Цель:** Максимально упростить развертывание
