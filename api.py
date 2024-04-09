import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.config import Config
from router.map_gen import mapGen

config = Config()
app = FastAPI(title="Luminara API",
            version=config.version,
            description="A RESTful API for Luminara.",
            docs_url="/docs",
              )

@app.get("/status")
async def status():
    return {"version": config.version, "buildid": config.buildid}

app.include_router(mapGen)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=443)