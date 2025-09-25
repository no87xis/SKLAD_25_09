# План чистки скриптов

**Дата создания:** 2025-09-25  
**Цель:** Сократить 58 скриптов до 8-12 ключевых

## 📋 Классификация по статусам

| Файл | Статус | Причина | Действие | Целевой файл |
|------|--------|---------|----------|--------------|
| **🐧 LINUX/MAC (.sh)** | | | | |
| `simple_deploy.sh` | **KEEP** | Главный скрипт развертывания | Оставить как есть | `simple_deploy.sh` |
| `deploy.sh` | **REMOVE** | Дублирует simple_deploy.sh | Удалить | - |
| `server_setup.sh` | **ARCHIVE** | Альтернативный вариант настройки | Архивировать | `scripts/ARCHIVE/` |
| `working_server_setup.sh` | **REMOVE** | Дублирует simple_deploy.sh | Удалить | - |
| `update_server_complete.sh` | **ARCHIVE** | Историческая ценность | Архивировать | `scripts/ARCHIVE/` |
| `update_server.sh` | **REMOVE** | Дублирует функциональность | Удалить | - |
| `ULTRA_PERFECT_server_setup.sh` | **REMOVE** | Избыточное название, дублирует | Удалить | - |
| `transfer_db.sh` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| `fix_server.sh` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| `quick_update.sh` | **REMOVE** | Дублирует обновления | Удалить | - |
| `quick_fix.sh` | **REMOVE** | Дублирует исправления | Удалить | - |
| `sync_from_github.sh` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| `quick_deploy.sh` | **REMOVE** | Дублирует simple_deploy.sh | Удалить | - |
| `step_by_step_deploy.sh` | **ARCHIVE** | Альтернативный подход | Архивировать | `scripts/ARCHIVE/` |
| `server_fix.sh` | **REMOVE** | Дублирует fix_server.sh | Удалить | - |
| `simple_server_setup.sh` | **REMOVE** | Дублирует simple_deploy.sh | Удалить | - |
| `proper_server_setup.sh` | **ARCHIVE** | Альтернативный вариант | Архивировать | `scripts/ARCHIVE/` |
| `perfect_server_setup.sh` | **REMOVE** | Избыточное название | Удалить | - |
| `clean_and_update.sh` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| `perfect_full_server_setup.sh` | **REMOVE** | Избыточное название | Удалить | - |
| `deploy_working_code.sh` | **REMOVE** | Дублирует simple_deploy.sh | Удалить | - |
| **🪟 WINDOWS CMD (.cmd)** | | | | |
| `scripts\win\make.bat` | **KEEP** | Главный Windows скрипт | Оставить как есть | `scripts/win/make.bat` |
| `scripts\win\serve_dev.cmd` | **KEEP** | Запуск dev-сервера | Оставить как есть | `scripts/win/serve_dev.cmd` |
| `scripts\win\serve_status.cmd` | **KEEP** | Проверка статуса | Оставить как есть | `scripts/win/serve_status.cmd` |
| `scripts\win\serve_stop.cmd` | **KEEP** | Остановка сервера | Оставить как есть | `scripts/win/serve_stop.cmd` |
| `scripts\win\test_server.cmd` | **EDIT** | Объединить с serve_status | Обновить | `scripts/win/serve_status.cmd` |
| `scripts\win\stop_simple.cmd` | **REMOVE** | Дублирует serve_stop.cmd | Удалить | - |
| `scripts\win\start_simple.cmd` | **REMOVE** | Дублирует serve_dev.cmd | Удалить | - |
| `scripts\win\check_simple.cmd` | **REMOVE** | Дублирует serve_status.cmd | Удалить | - |
| `scripts\win\commit_changes.cmd` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| `scripts\win\restart_server.cmd` | **EDIT** | Объединить логику | Обновить | `scripts/win/restart_server.cmd` |
| `scripts\win\push_changes.cmd` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| `scripts\win\fix_admin_role.cmd` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| `scripts\win\fix_imports.cmd` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| `scripts\win\deploy_status.cmd` | **REMOVE** | Дублирует serve_status.cmd | Удалить | - |
| `scripts\win\create_admin.cmd` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| `scripts\win\fix_admin.cmd` | **REMOVE** | Дублирует create_admin.cmd | Удалить | - |
| `scripts\win\fix_db.cmd` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| **🪟 WINDOWS BATCH (.bat)** | | | | |
| `auto_commands.bat` | **REMOVE** | Временный файл | Удалить | - |
| `transfer_db.bat` | **REMOVE** | Дублирует .sh версию | Удалить | - |
| `start_server.bat` | **REMOVE** | Дублирует serve_dev.cmd | Удалить | - |
| `start_server_ULTRA_STABLE.bat` | **REMOVE** | Избыточное название | Удалить | - |
| `start_server_stable.bat` | **REMOVE** | Дублирует serve_dev.cmd | Удалить | - |
| `deploy.bat` | **REMOVE** | Дублирует simple_deploy.sh | Удалить | - |
| `scripts\dev.bat` | **ARCHIVE** | Альтернативный подход | Архивировать | `scripts/ARCHIVE/` |
| `scripts\health_check.bat` | **EDIT** | Объединить с serve_status | Обновить | `scripts/win/serve_status.cmd` |
| `scripts\start_server.bat` | **REMOVE** | Дублирует serve_dev.cmd | Удалить | - |
| **🐚 POWERSHELL (.ps1)** | | | | |
| `setup_auto_mode.ps1` | **REMOVE** | Временный файл | Удалить | - |
| `start_server_ULTRA_STABLE.ps1` | **REMOVE** | Избыточное название | Удалить | - |
| `start_server_stable.ps1` | **REMOVE** | Дублирует ops/start.ps1 | Удалить | - |
| `start_server.ps1` | **REMOVE** | Дублирует ops/start.ps1 | Удалить | - |
| `run_diagnosis.ps1` | **ARCHIVE** | Специальная функция | Архивировать | `scripts/ARCHIVE/` |
| `scripts\dev.ps1` | **ARCHIVE** | Альтернативный подход | Архивировать | `scripts/ARCHIVE/` |
| `ops\start.ps1` | **KEEP** | Операционный запуск | Оставить как есть | `ops/start.ps1` |
| `ops\status.ps1` | **KEEP** | Операционный статус | Оставить как есть | `ops/status.ps1` |
| `ops\stop.ps1` | **KEEP** | Операционная остановка | Оставить как есть | `ops/stop.ps1` |
| `ops\restart.ps1` | **KEEP** | Операционный перезапуск | Оставить как есть | `ops/restart.ps1` |
| `ops\health.ps1` | **KEEP** | Операционная проверка | Оставить как есть | `ops/health.ps1` |

## 📊 Статистика по статусам

| Статус | Количество | Процент |
|--------|------------|---------|
| **KEEP** | 10 | 17% |
| **EDIT** | 3 | 5% |
| **ARCHIVE** | 12 | 21% |
| **REMOVE** | 33 | 57% |
| **ИТОГО** | 58 | 100% |

## 🎯 Результат после чистки

**Будет оставлено:** 10 основных скриптов  
**Будет обновлено:** 3 скрипта  
**Будет заархивировано:** 12 скриптов  
**Будет удалено:** 33 скрипта  

**Сокращение:** с 58 до 10 файлов (-83%)

## 🔧 План выполнения

1. ✅ **Инвентаризация** - завершена
2. 🔄 **Классификация** - завершена  
3. ⏳ **Создание резервной копии**
4. ⏳ **Архивирование (12 файлов)**
5. ⏳ **Удаление (33 файла)**
6. ⏳ **Обновление (3 файла)**
7. ⏳ **Создание итогового отчета**
