from fastapi import FastAPI,APIRouter

from core.config import Config


mapGen = APIRouter()

@mapGen.get("/generate/{pos}")
async def generate_map(pos: str):
    config=Config()
    pos1,pos2 = pos.split(",")
    return {"version": config.version, "pos1": pos1, "pos2": pos2}