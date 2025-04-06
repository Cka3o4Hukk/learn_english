from fastapi import APIRouter
from typing import List

from app.categories.repo import CategoryRepo
from app.categories.schemas import SCategory

router = APIRouter(
    prefix="/categories",
    tags=["Категории"]
)

@router.get("")
async def get_category() -> List[SCategory]:
    return await CategoryRepo.find_all()