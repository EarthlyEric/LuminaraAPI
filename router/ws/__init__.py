from fastapi import APIRouter, WebSocket
from libs.utils.tokenGen import verifyAccessToken

ws = APIRouter(
    prefix="/ws"
    tags=["websocket"]
)

@ws.websocket()
async def websocketEndpoint(websocket: WebSocket):
    token = websocket.headers.get("sec-websocket-protocol")
    user_uuid = await ver
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
