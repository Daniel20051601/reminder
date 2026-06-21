from contextlib import contextmanager
from app.database.session import SessionLocal
from app.repositories.reminder_repository import ReminderRepository
from app.services.reminder_service import ReminderService

@contextmanager
def reminder_service():
    
    db = SessionLocal()
    
    try:
        yield ReminderService(ReminderRepository(db))
    finally:
        db.close()