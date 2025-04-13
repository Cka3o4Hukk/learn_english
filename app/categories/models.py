from sqlalchemy import Column, Integer, String
from app.database import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    icon = Column(Integer, default=None)