from fastapi import APIRouter
from .map import map

utils = APIRouter(
    prefix="/utils",
    tags=["utils"]
)

utils.include_router(map)