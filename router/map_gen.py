from fastapi import FastAPI,APIRouter

from core.config import Config
from core.libs.map import Map


mapGen = APIRouter()

@mapGen.get("/generate/{pos}")
async def generate_map(pos: str):
    config = Config()
    pos1,pos2 = pos.split(",")
    location = [pos1,pos2]
    image = await Map.generate(location)

    return {
        "version": config.version, 
        "pos1": pos1, "pos2": pos2, 
        "image": image}