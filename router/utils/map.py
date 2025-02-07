from fastapi import APIRouter, HTTPException
from fastapi import Depends

from libs.config import config
from libs.utils.mapGen import Map
from libs.utils.tokenGen import verifyAccessToken

map = APIRouter(
    prefix="/map"
)

@map.get("/generateMapImages",
         summary="Generate a map image with a marker",
         description="Generate a map image with a marker at the specified location, and return the image as a base64 string",
        )
async def generate_map(pos: str, payload: str = Depends(verifyAccessToken)):
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    pos1,pos2 = pos.split(",")
    location = [pos1,pos2]
    image = await Map.generate(location)

    return {
        "version": config.version, 
        "pos1": pos1, 
        "pos2": pos2, 
        "image": image
        }