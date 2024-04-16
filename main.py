from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends
from typing import Annotated


app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: str | None

class STask(STaskAdd):
    id: int

tasks = []
 
@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],

):
    tasks.append(task)
    return {"ok": True}

# @app.get("/tasks")
# def get_tasks():
#   task = Task(name="Write the video", description="for the manager")
#   return {"data": task}
