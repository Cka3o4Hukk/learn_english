from sqlalchemy import Column, Integer, String
from app.database import Base

class Word(Base):
    __tablename__ = "word"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    transcription = Column(String)
    example = Column(String, nullable=False)
    # sound = Column(url or sound)