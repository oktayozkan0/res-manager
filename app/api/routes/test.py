from starlette.requests import Request
from fastapi import APIRouter, Depends
from app.db.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.test import TestCreateSchema, TestUpdateSchema
from app.db.models.test import Test
from app.services.test import get_test_service, create_test_service, update_test_service, return_host_ip


router = APIRouter()

@router.post("/icreate")
async def create_test(
    payload: TestCreateSchema,
    db: AsyncSession = Depends(get_db)
):
    return await create_test_service(db, payload)

@router.get("/iget")
async def get_test(
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    return await get_test_service(db=db)

@router.post("/iupdate")
async def update_test(
    payload: TestUpdateSchema,
    db: AsyncSession = Depends(get_db)
):
    return await update_test_service(db=db, payload=payload)
