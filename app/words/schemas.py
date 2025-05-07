from typing import Optional

from pydantic import BaseModel


class SWord(BaseModel):
    id: int
    name: str
    translation: str
    transcription: Optional[str]
    example: str
