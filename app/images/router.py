from fastapi import APIRouter, UploadFile
import shutil

router = APIRouter(
    prefix="/icons",
    tags=["Картинки категорий"]
)

@router.post("/categories")
async def add_category_icon(name: int, file: UploadFile):
    with open(f"app/static/icons/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)