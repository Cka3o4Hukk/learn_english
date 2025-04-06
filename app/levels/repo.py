from sqlalchemy import select

from app.database import async_session_maker
from app.levels.models import Levels
from app.repo.base import BaseRepo


class LevelRepo(BaseRepo):
    model = Levels        
