from fastapi import FastAPI

app = FastAPI(title="Dev Container uv Sync Demo")


@app.get("/")
def say_hello():
    return {"message": "Hello World!", "status": "소스 동기화 작동 중"}