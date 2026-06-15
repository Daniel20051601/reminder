from app.database.session import SessionLocal
from app.models.reminder import Reminder
from app.models.status import Status
from app.models.user import User
from app.models.category import Category
from app.database.seeders.category_seeders import seed_categories
from app.database.seeders.status_seeders import seed_status


def run_seeders():
    
    db = SessionLocal()
    
    try:
        seed_categories(db)
        seed_status(db)
        print("Tables updated")
    finally:
        db.close()

if __name__ == "__main__":
    run_seeders()