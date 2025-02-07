from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager

from core.config import config
from core import database
from router.auth import auth
from router.utils import utils

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.init_db()
    yield

app = FastAPI(title="Luminara API",
            version=config.version,
            description="A RESTful API for Luminara.",
            docs_url="/docs",
            redoc_url=None,
            lifespan=lifespan
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

@app.get("/status"
         ,summary="Get the status of the API"
            ,description="Get the version, build ID and Bot status from the API"
         )
async def status():
    return {"version": config.version, "build_id": config.build_id}

app.include_router(utils)
app.include_router(auth)