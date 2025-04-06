from pydantic import BaseModel


class SCategory(BaseModel):
    id: int
    name: str
