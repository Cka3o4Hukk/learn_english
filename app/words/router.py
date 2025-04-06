from fastapi import APIRouter
from typing import List

from app.words.repo import WordRepo
from app.words.schemas import SWord

router = APIRouter(
    prefix="/words",
    tags=["Слова"]
)

@router.get("")
async def get_levels()-> SWord: # ошибка, если нашего слова нет
    return await WordRepo.find_by_id(2)