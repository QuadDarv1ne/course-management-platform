from fastapi import APIRouter, WebSocket
from typing import List

router = APIRouter()

clients: List[WebSocket] = []

# Уведомление через WebSocket
@router.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except:
        clients.remove(websocket)
