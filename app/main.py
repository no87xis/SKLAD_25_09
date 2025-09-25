from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.orm import Session
from .config import settings
from .db import engine, Base, get_db
from .routers import (
    web_public,
    web_products,
    web_orders,
    web_analytics,
    web_admin_panel,
    api,
    web_shop,
    shop_api,
    shop_admin,
    qr_scanner,
    delivery_payment,
    delivery_notifications,
)
from .services.auth import get_current_user_optional
import logging

# Configure logging
log_level = getattr(logging, settings.log_level.upper(), logging.INFO)
logging.basicConfig(
    level=log_level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("sirius.log", encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)

# Self-check: validate imports and configuration
try:
    logger.info("🚀 Запуск приложения Sirius Sklad")
    logger.info("🔧 Проверка импортов роутеров...")
    # All routers are imported above, if there's an error it will be caught here
    logger.info("✅ Все роутеры импортированы успешно")
    
    logger.info("🔧 Проверка конфигурации...")
    logger.info(f"✅ Environment: {settings.environment}")
    logger.info(f"✅ Debug mode: {settings.debug}")
    logger.info(f"✅ Log level: {settings.log_level}")
    logger.info(f"✅ Database URL: {settings.database_url[:20]}...")
    
    # Check optional services
    if settings.telegram_bot_token:
        logger.info("✅ Telegram notifications: настроены")
    else:
        logger.info("ℹ️ Telegram notifications: не настроены")
        
    if settings.smtp_host:
        logger.info("✅ Email notifications: настроены")
    else:
        logger.info("ℹ️ Email notifications: не настроены")
    
except Exception as e:
    logger.error(f"❗ Ошибка при инициализации: {e}")
    raise

# Create tables only in development mode
if settings.environment == "development" and settings.debug:
    logger.info("🔧 Создание таблиц в development режиме...")
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Таблицы созданы успешно")
else:
    logger.info("ℹ️ Production режим: таблицы создаются через миграции")

# Create FastAPI app
app = FastAPI(
    title="Сириус - Система учёта склада",
    description="Веб-приложение для управления складом, заказами и поставками",
    version="1.0.0"
)

# Add session middleware
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.secret_key,
    max_age=settings.session_max_age,
    same_site="lax",  # Улучшенная совместимость с браузерами
    https_only=False  # Разрешаем HTTP для локальной разработки
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Include routers
app.include_router(web_public.router)
app.include_router(web_products.router)
app.include_router(web_orders.router)
app.include_router(web_analytics.router, prefix="/admin")
app.include_router(web_admin_panel.router)
app.include_router(api.router, prefix="/api")
app.include_router(shop_api.router)  # API роутер должен быть ПЕРЕД web_shop
app.include_router(web_shop.router)  # Web роутер подключается ПОСЛЕ API
app.include_router(shop_admin.router)
app.include_router(qr_scanner.router)
app.include_router(delivery_payment.router)
app.include_router(delivery_notifications.router)

# Роуты для основных страниц
@app.get("/")
async def root(request: Request, db: Session = Depends(get_db)):
    """Главная страница"""
    current_user = get_current_user_optional(request, db)
    return templates.TemplateResponse("index.html", {"request": request, "current_user": current_user})


@app.get("/health")
@app.head("/health")
async def health_check():
    """Быстрая проверка здоровья приложения"""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
