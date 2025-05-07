from app.repo.base import BaseRepo
from app.words.models import Word


class WordRepo(BaseRepo):
    model = Word
