import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

from core.config import Config
from router.map_gen import mapGen

config = Config()
app = FastAPI(title="Luminara API",
            version=config.version,
            description="A RESTful API for Luminara.",
            docs_url="/docs",
            redoc_url=None
              )
app.mount("/", StaticFiles(directory="static",html=True), name="static")

@app.get("/status")
async def status():
    return {"version": config.version, "buildid": config.buildid}

app.include_router(mapGen)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=443)