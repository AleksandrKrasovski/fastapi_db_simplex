from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: str | None

class STask(STaskAdd):
    id: int

    model_config: ConfigDict(from_attributes=True) # type: ignore

class STaskId(BaseModel):
    ok: bool = True
    id: int