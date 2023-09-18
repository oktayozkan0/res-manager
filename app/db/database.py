from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker


engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@localhost/test",
    future=True,
    echo=True,
)

AsyncSessionFactory = async_sessionmaker(engine, autoflush=False, expire_on_commit=False,)


# Dependency
async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        yield session
