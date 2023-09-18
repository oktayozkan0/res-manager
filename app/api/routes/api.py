from fastapi import APIRouter

import app.api.routes.test as test


router = APIRouter()
router.include_router(test.router)
