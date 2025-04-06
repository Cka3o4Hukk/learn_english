from pydantic import BaseModel


class SWord(BaseModel):
    id: int
    name: str
    translation: str
    transcription: str
    example: str

    # class Config:
    #     orm_mode = True
