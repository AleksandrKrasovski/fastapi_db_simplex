from fastapi import FastAPI
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
