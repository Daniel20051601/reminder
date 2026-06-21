from app.models.category import Category
from app.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository
    
    def get_categories(self) -> list[Category]:
        return self.repository.get_all()