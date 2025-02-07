from contextlib import asynccontextmanager
import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from sqlalchemy.sql import insert, func

from .schema import ApiKey, Base
from core.config import config
from core.utils.tokenGen import generateAPIKey

DATABASE_URL = f"postgresql+asyncpg://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"

engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False 
)

@asynccontextmanager
async def getSession():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

async def initDatabase():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Database tables created")
async def resetDatabase():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        print("All tables have been dropped.")
        
async def createRootAPIKey():
    async with getSession() as session:
        result = await session.execute(
            select(func.count(ApiKey.uuid)).filter(ApiKey.level == 3)
        )
        rootApiKeyCount = result.scalar()
        if rootApiKeyCount == 0:
            apiKey = generateAPIKey()
            newRootApiKey = ApiKey(
                apiKey=apiKey,
                level=3
                )
            session.add(newRootApiKey)
            with open('api_key.txt','w') as f:
                f.write(apiKey)
            print("Root API key written to api_key.txt")
        else:
            print("Root API key already exists")
            result = await session.execute(select(ApiKey).where(ApiKey.level == 3))
            item = result.scalars().first()
            with open('api_key.txt','w') as f:
                f.write(item.apiKey)
            print("Root API key written to api_key.txt")
            