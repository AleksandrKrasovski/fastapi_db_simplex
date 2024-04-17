from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Annotated
from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DATABASE is cleared")
    await create_tables()
    print("DATABASE is ready")
    yield
    print("DATABASE off")


app = FastAPI(lifespan=lifespan)


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
