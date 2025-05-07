from typing import Optional

from pydantic import BaseModel


class SCategory(BaseModel):
    id: int
    name: str
    icon: Optional[int]
