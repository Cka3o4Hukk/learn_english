from sqlalchemy import select

from app.database import async_session_maker


class BaseRepo:
    model = None 

    @classmethod
    async def find_by_id(cls, word_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=word_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()  # mappings