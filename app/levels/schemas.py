from pydantic import BaseModel


class SLevel(BaseModel):
    id: int
    name: str
    code: str
