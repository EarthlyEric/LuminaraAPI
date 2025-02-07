from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import msgpack
from libs.utils.tokenGen import verifyAccessToken

ws = APIRouter(
    prefix="/ws",
    tags=["websocket"]
)

@ws.websocket("")
async def websocketEndpoint(websocket: WebSocket):
    token = websocket.headers.get("sec-websocket-protocol")
    payload = verifyAccessToken(token)
    if not payload:
        await websocket.close(code=1008)
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            try:
                message = msgpack.unpackb(data, raw=False)
            except Exception as e:
                    msg = {"error": "Invalid MessagePack data", "detail": str(e)}
                    error_response = msgpack.packb(
                        msg,
                        use_bin_type=True
                    )
                    await websocket.send_bytes(error_response)
                    continue
            print(message)
        
            response_data = {
                "message": "Hello from the server!"
            }
        
            response = msgpack.packb(
                response_data,
                use_bin_type=True
            )
            await websocket.send_bytes(response)
    except WebSocketDisconnect:
        print("Client disconnected")
