import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[3]))
import asyncio
from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.settings.app import AppSettings

from app.db.models.base import Base


target_metadata = Base.metadata

settings = AppSettings()
DB_URL = settings.database_url

def do_run_migrations(connection):
    context.configure(
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
        connection=connection,
        target_metadata=target_metadata,
        include_schemas=True,
        # literal_binds=True,
        version_table_schema=target_metadata.schema,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_async_engine(settings.database_url.unicode_string(), future=True)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


asyncio.run(run_migrations_online())
