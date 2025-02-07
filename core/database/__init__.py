from contextlib import asynccontextmanager
import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .model import Base
from core.config import config

DATABASE_URL = f"postgresql+asyncpg://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"

engine = create_async_engine(DATABASE_URL, echo=config.database_debug)

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False 
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logging.info("Database tables created")

@asynccontextmanager
async def getSession():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
