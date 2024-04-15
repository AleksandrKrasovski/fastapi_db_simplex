from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Task(BaseModel):
  name: str
  description: str | None


@app.get("/tasks")
def get_tasks():
  task = Task(name="Write the video", description="for the manager")
  return {"data": task}
