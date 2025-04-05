from sqlalchemy import Column, Integer, String
from app.database import Base

class Levels(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)


# class Category(Base):
#     __tablename__ = "category"

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     icon = Column(Images)