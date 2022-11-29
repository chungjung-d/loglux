from fastapi import APIRouter

from route import nginx

router = APIRouter

router.include_router(nginx.router, tags=["nginx"], prefix="/nginx")