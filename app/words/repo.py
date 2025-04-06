from app.words.models import Word
from app.repo.base import BaseRepo

class WordRepo(BaseRepo):
    model = Word   