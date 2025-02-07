from fastapi import APIRouter
from router.auth.token import token 

auth = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

auth.include_router(token)
  