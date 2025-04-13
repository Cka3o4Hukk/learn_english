from pydantic import BaseModel
from typing import Optional



class SCategory(BaseModel):
    id: int
    name: str
    icon: Optional[int]
