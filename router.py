from fastapi import APIRouter, Depends
from typing import Annotated

from schemas import STaskAdd, STask


router = APIRouter()

tasks = []

@router.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}
 
# @router.get("/tasks")
# def get_tasks():
#   task = Task(name="Write the video", description="for the manager")
#   return {"data": task}