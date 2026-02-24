from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import psutil
import asyncio

app = FastAPI()

@app.websocket('/ws/~~')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        pass
    except WebSocketDisconnect:
        print('웹소켓 연결 해제')
