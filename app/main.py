from fastapi import FastAPI
from injector import logger

app = FastAPI(title="Dev Container uv Sync Demo")


@app.get("/")
def say_hello():
    logger.info(f"Devcontainer Request..~~")
    return {"message": "Hello World!", "status": "소스 동기화 작동 중"}