from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.categories.router import router as router_categories
from app.images.router import router as router_images
from app.levels.router import router as router_levels
from app.words.router import router as router_words

# STATIC = "static"

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_categories)
app.include_router(router_images)
app.include_router(router_levels)
app.include_router(router_words)

