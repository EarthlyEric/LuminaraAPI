from fastapi import FastAPI

from core.config import Config
from router.map_gen import mapGen

config = Config()
app = FastAPI(title="Luminara API",
            version=config.version,
            description="A RESTful API for Luminara.",
            docs_url="/",
              )

@app.get("/ping")
async def root():
    return {"version": config.version}

app.include_router(mapGen)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=443)