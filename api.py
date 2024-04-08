from fastapi import FastAPI

from core.config import Config
from router.map_gen import mapGen

app = FastAPI()

@app.get("/")
async def root():
    config=Config()
    return {"version": config.version}

app.include_router(mapGen)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=443)