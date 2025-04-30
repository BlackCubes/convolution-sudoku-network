from fastapi import APIRouter
from fastapi import WebSocket

from csn.websocket.sudoku import router as sudoku_ws_router

ws_router = APIRouter()


@ws_router.websocket("/healthcheck")
async def healthcheck(websocket: WebSocket):
    await websocket.accept()

    await websocket.send_json({"status": "ok"})

    await websocket.close()


ws_router.include_router(
    router=sudoku_ws_router,
    prefix="/sudokus",
    tags=["sudokus"],
)
