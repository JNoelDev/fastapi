from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker
from app.core.config import get_settings

settings=get_settings()

engine=create_async_engine(
    settings.database_url,
    pool_pre_ping=True,
    connect_args={
        "statement_cache_size": 0
    }
)

SessionLocal = async_sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession,None]:
    async with SessionLocal() as session:
        yield session