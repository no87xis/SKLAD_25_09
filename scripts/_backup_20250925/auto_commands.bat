@echo off
echo ========================================
echo    АВТОМАТИЧЕСКОЕ ВЫПОЛНЕНИЕ КОМАНД
echo ========================================
echo.

echo [1/5] Проверка статуса Git...
git status
echo.

echo [2/5] Добавление всех изменений...
git add .
echo.

echo [3/5] Создание коммита...
git commit -m "📚 Complete documentation cleanup and reorganization

- ✅ Processed 48 → 21 files (-56% reduction)
- ✅ Eliminated all duplicates and conflicts  
- ✅ Created unified deployment guides
- ✅ Updated README as main entry point
- ✅ Preserved all important information
- ✅ Created backup and archive systems

Key documents:
- README.md (main entry point)
- DEPLOYMENT.md (unified deployment guide) 
- SERVER_GUIDE.md (server management)
- SIMPLE_GUIDE.md (beginner-friendly)

Archive: docs/ARCHIVE/ (7 files)
Backup: docs/_backup_20250925/ + doc/_backup_20250925/"
echo.

echo [4/5] Проверка финального статуса...
git status
echo.

echo [5/5] Показ последних коммитов...
git log --oneline -3
echo.

echo ========================================
echo ✅ ВСЕ КОМАНДЫ ВЫПОЛНЕНЫ АВТОМАТИЧЕСКИ!
echo ========================================
pause
