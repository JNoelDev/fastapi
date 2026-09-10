from fastapi import FastAPI
from app.core.config import get_settings
from app.modules.users.register.router import router as register_router

settings=get_settings()

app=FastAPI(
    title=settings.app_name,
    docs_url="/my_api/docs" if settings.environment=="development" else None,
    redoc_url="/my_api/redoc" if settings.environment=="development" else None,
)

app.include_router(register_router,prefix=settings.prefix_app)