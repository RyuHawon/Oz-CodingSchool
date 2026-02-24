from fastapi import WebSocket, WebSocketDisconnect, FastAPI
from typing import List
app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for conn in self.active_connections:
            await conn.send_json(message)

manager = ConnectionManager()


@app.websocket('/ws/chat/{client_name}')
async def websocek_endpoint(websocket: WebSocket, client_name: str):
    await manager.connect(websocket)

    # {
    #     'type':, (system: 공지, ?: 유저채팅)
    #     'message':, (사용자가 보내는 메시지)
    #     'sender': (client_name)
    # }

    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(
                {
                    'type': 'chat',
                    'message': data,
                    'sender': client_name
                }
            )
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(
            {
                'type': 'system',
                'message': f'{client_name}님이 퇴창하셨습니다.'
            }
        )
