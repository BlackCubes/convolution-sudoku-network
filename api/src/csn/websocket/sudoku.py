import asyncio
import math

from fastapi import APIRouter
from fastapi import WebSocket

from csn.sudoku.service import example

router = APIRouter()


@router.websocket("/example")
async def read_example(websocket: WebSocket):
    await websocket.accept()

    try:
        data = example()
        total_steps = data["length"]

        initial_delay = 1.0
        min_delay = 0.01

        for step_index, step in enumerate(data["steps"]):
            step_data = {"row": step[0], "col": step[1], "num": step[2]}

            await websocket.send_json(step_data)

            progress = step_index / total_steps
            current_delay = initial_delay * math.exp(-6 * progress)
            delay = max(current_delay, min_delay)

            await asyncio.sleep(delay)

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
