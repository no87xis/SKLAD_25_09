# Настройка автоматического режима для Cursor
Write-Host "🔧 Настройка автоматического режима..." -ForegroundColor Green

# Создание профиля PowerShell для автоматических команд
$profileContent = @"
# Автоматическое выполнение команд для Cursor AI
function Auto-Git-Status { git status }
function Auto-Git-Add { git add . }
function Auto-Git-Commit { param($msg) git commit -m $msg }
function Auto-Git-Log { git log --oneline -5 }

# Алиасы для быстрого доступа
Set-Alias -Name gs -Value Auto-Git-Status
Set-Alias -Name ga -Value Auto-Git-Add
Set-Alias -Name gl -Value Auto-Git-Log

Write-Host "✅ Автоматические команды настроены!" -ForegroundColor Green
Write-Host "Используйте: gs, ga, gl" -ForegroundColor Yellow
"@

# Сохранение профиля
$profileContent | Out-File -FilePath $PROFILE -Encoding UTF8
Write-Host "✅ Профиль PowerShell создан: $PROFILE" -ForegroundColor Green

# Инструкции
Write-Host "`n📋 Инструкции:" -ForegroundColor Cyan
Write-Host "1. Перезапустите Cursor" -ForegroundColor White
Write-Host "2. Откройте терминал в Cursor" -ForegroundColor White  
Write-Host "3. Команды будут выполняться автоматически" -ForegroundColor White
Write-Host "`nИли просто запустите auto_commands.bat" -ForegroundColor Yellow
