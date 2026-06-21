from contextlib import contextmanager
from app.database.session import SessionLocal
from app.repositories.category_repository import CategoryRepository
from app.services.category_service import CategoryService

@contextmanager
def category_service():
    
    db = SessionLocal()
    
    try:
        yield CategoryService(CategoryRepository(db))
    finally:
        db.close()