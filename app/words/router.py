from fastapi import APIRouter

from app.words.repo import WordRepo
from app.words.schemas import SWord

router = APIRouter(
    prefix="/words",
    tags=["Слова"]
)

@router.get("/{number}")
async def get_levels(number: int)-> SWord:
    return await WordRepo.find_by_id(number)