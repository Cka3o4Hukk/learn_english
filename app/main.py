from fastapi import FastAPI
from pydantic import BaseModel

from app.levels.router import router as router_levels
from app.categories.router import router as router_categories
from app.words.router import router as router_words

app = FastAPI()

app.include_router(router_levels)
app.include_router(router_categories)
app.include_router(router_words)

