from fastapi import APIRouter
from core.config import Config

from core.utils.mapGen import Map

map = APIRouter(
    prefix="/map"
)

@map.get("/generateMapImages",
         summary="Generate a map image with a marker",
         description="Generate a map image with a marker at the specified location, and return the image as a base64 string",
        )
async def generate_map(pos: str):
    config = Config()
    pos1,pos2 = pos.split(",")
    location = [pos1,pos2]
    image = await Map.generate(location)

    return {
        "version": config.version, 
        "pos1": pos1, "pos2": pos2, 
        "image": image}