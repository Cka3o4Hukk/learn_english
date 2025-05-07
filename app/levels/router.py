from typing import List

from fastapi import APIRouter

from app.levels.repo import LevelRepo
from app.levels.schemas import SLevel

router = APIRouter(prefix="/levels", tags=["Уровни английского языка"])


@router.get("")
async def get_levels() -> List[SLevel]:
    return await LevelRepo.find_all()
