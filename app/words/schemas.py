from pydantic import BaseModel
from typing import Optional


class SWord(BaseModel):
    id: int
    name: str
    translation: str
    transcription: Optional[str]
    example: str
