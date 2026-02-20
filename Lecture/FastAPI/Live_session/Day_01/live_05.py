import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_async_item():
    await asyncio.sleep(1)
    return {"message": "async 연습"}
