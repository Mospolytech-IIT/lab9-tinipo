from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Создание движка базы данных
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Создание сессии
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Инициализация базы данных
async def init_db():
    from app.models import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
