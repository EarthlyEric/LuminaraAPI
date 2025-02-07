from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.database import getSession
from core.database.schema import ApiKey
from core.utils.tokenGen import createAccessToken

token = APIRouter(
    prefix="/token",
)

class generateJWTtokenResponse(BaseModel):
    apiKey: str

@token.post("",
            summary="Generate a JWT token",
            description="Generate a JWT token for the user's API key",
            )
async def generateJWTtoken(response: generateJWTtokenResponse, database: AsyncSession = Depends(getSession)):
    async with database as session:
        result = await session.execute(select(ApiKey).where(ApiKey.apiKey == response.apiKey))
    item = result.scalars().first()
    if item is None:
        raise HTTPException(status_code=401, detail="Your API key is invalid")
    else:
        return {"accessTocken": createAccessToken({"uuid": str(item.uuid), "apiKey": item.apiKey})}
    