from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app.db.models.test import Test
from app.schemas.test import TestCreateSchema, TestUpdateSchema


async def get_test_service(db: AsyncSession):
    stmt = select(Test)
    result = await db.execute(stmt)
    return result.scalars().all()

async def create_test_service(db: AsyncSession, payload: TestCreateSchema):
    data = Test(**payload.model_dump())
    db.add(data)
    await db.commit()
    return {"msg": "created"}

async def update_test_service(db: AsyncSession, payload: TestUpdateSchema):
    stmt = select(Test).where(Test.id == payload.id)
    result = await db.execute(stmt)
    instance = result.scalars().first()

    if not instance:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found"
        )

    update_stmt = update(Test).where(Test.id == payload.id).values(test_col=payload.new_col)
    res = await db.execute(update_stmt)
    await db.commit()
    return res
