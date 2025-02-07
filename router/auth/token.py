from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.database import getSession
from core.database.model import ApiKey
from core.utils.tokenGen import createAccessToken
import uuid

token = APIRouter(
    prefix="/token",
)

fake_api_key = "1234"

class generateJWTtokenResponse(BaseModel):
    apiKey: str

@token.post("",
            summary="Generate a JWT token",
            description="Generate a JWT token for the user's API key",
            )
async def generateJWTtoken(response: generateJWTtokenResponse, database: AsyncSession = Depends(getSession)):
    cmd = select(ApiKey).where(ApiKey.apiKey == response.apiKey)
    async with database as session:
        result = await session.execute(cmd)
    item = result.scalars().first()
    if item is None:
        raise HTTPException(status_code=401, detail="Your API key is invalid")
    else:
        return {"accessTocken": createAccessToken({"uuid": item.uuid, "apiKey": item.apiKey})}
    