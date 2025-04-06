from app.categories.models import Category
from app.repo.base import BaseRepo

class CategoryRepo(BaseRepo):
    model = Category        
