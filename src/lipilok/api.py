from fastapi import APIRouter
from .routers.endpoints import router as base_endpoints

router = APIRouter(prefix="/api/v1")

router.include_router(base_endpoints)
