from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
# from sqlalchemy import  Column, Integer, String

from app.config import settings
 
# Движок
engine = create_async_engine(settings.DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase): 
    """Базовый класс для моделей."""

    pass
 
'''# создаем модель, объекты которой будут храниться в бд
class Level(Base):
    __tablename__ = "people"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(Integer)
 
# создаем таблицы
Base.metadata.create_all(bind=engine)
'''