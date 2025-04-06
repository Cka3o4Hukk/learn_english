from fastapi import FastAPI
from pydantic import BaseModel

from app.levels.router import router as router_levels

app = FastAPI()

app.include_router(router_levels)
