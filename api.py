import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from core.config import Config
from router.map_gen import mapGen

config = Config()
app = FastAPI(title="Luminara API",
            version=config.version,
            description="A RESTful API for Luminara.",
            docs_url="/docs",
            redoc_url=None
              )
app.mount("/static", StaticFiles(directory="static",html=True), name="static")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico",status_code=200)

@app.get("/",include_in_schema=False)
async def index():
    return HTMLResponse(content=open("static/index.html", encoding="UTF-8").read(), status_code=200)

@app.get("/music",include_in_schema=False)
async def index():
    return HTMLResponse(content=open("static/music.html", encoding="UTF-8").read(), status_code=200)

@app.get("/status")
async def status():
    return {"version": config.version, "buildid": config.buildid}

app.include_router(mapGen)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=443)