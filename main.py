from fastapi import Depends, FastAPI
import uvicorn
from typing_extensions import Annotated
from functools import lru_cache
from utils import config

app = FastAPI(title = "WhatsApp Bot")

@lru_cache
def get_settings():
    """Using lru_cache decorator can prevent constantly loading the setting. 

    Returns:
        _type_: _description_
    """
    return config.Settings()


@app.get("/")
async def root():
    """This is only for testing.

    Returns:
        dict: a hellow world message
    """
    return {"message": "Hello World"}

@app.get("/info")
async def info(settings: Annotated[config.Settings, Depends(get_settings)]):
    """This is a testing section

    Returns:
        _type_: _description_
    """
    return {"access_token": settings.access_token}

@app.post("/webhook_endpoint", tags=["webhook"])
async def handle_webhook_evenet():

    return {"message": True}


if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",
        host = "127.0.0.1",
        port = 9999,
        reload=True,
        reload_includes=".py",
        log_level="info"
    )
    server = uvicorn.Server(config)
    server.run()