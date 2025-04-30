import asyncio

from fastapi import APIRouter
from fastapi import WebSocket

from csn.sudoku.service import example

router = APIRouter()


@router.websocket("/example")
async def read_example(websocket: WebSocket):
    await websocket.accept()

    try:
        data = example()

        for step in data["steps"]:
            step_data = {"row": step[0], "col": step[1], "num": step[2]}

            await websocket.send_json(step_data)

            await asyncio.sleep(1)

        await websocket.send_json(
            {
                "status": "complete",
                "total_steps": data["length"],
            }
        )

    except Exception as e:
        await websocket.send_json({"error": str(e)})

    finally:
        await websocket.close()
