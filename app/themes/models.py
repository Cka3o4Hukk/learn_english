from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

# class BaseTheme(Base):
    # pass


class Themes(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True)
    category = Column(ForeignKey("category.id"))
    level = Column(ForeignKey("levels.id"))
    name = Column(String, nullable=False)
    # photo = Column(url or image)

class Theme(Base):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True)
    category = Column(ForeignKey("category.id"))
    level = Column(ForeignKey("levels.id"))
    name = Column(String, nullable=False)
    # photo = Column(url or image)
    # words = list (id+name)
