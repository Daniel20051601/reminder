from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from app.models.reminder import Reminder
from app.models.status import Status
from app.models.user import User
from app.models.category import Category

# TODO The repository must implement an interface

class ReminderRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def create(self, reminder: Reminder, ) -> Reminder:
        
        self.db.add(reminder)
        self.db.commit()
        self.db.refresh(reminder)
        
        return reminder
    
    def get_by_id(self, id: int) -> Reminder | None:
        
        return (self.db.query(Reminder)
                        .filter(Reminder.reminder_id == id)
                        .first()
        )
    
    def get_all(self) -> list[Reminder]:
        
        return (self.db.query(Reminder)
                .join(Status)
                .filter(
                    # TODO Hacer esto usando constantes
                    Status.title.in_(["Pending", "Overdue"])
                )
                .order_by(Reminder.created_date.desc())
                        .all()   
        )
    
    def update(self, reminder: Reminder) -> Reminder:
        
        self.db.commit()
        self.db.refresh(reminder)
        
        return reminder
    
    def delete(self, reminder: Reminder) -> None:
        
        reminder.status_id = 8
        
        self.db.commit()
        
        self.db.refresh(reminder)
        
    def reminders_by_category(self, category_id: int) -> list[Category]:
        return (self.db.query(Reminder)
                .join(Status)
                    .filter(
                            Reminder.category_id == category_id,
                            Status.title.in_(["Pending", "Overdue"])
                    )
                    .order_by(Reminder.created_date.desc())
                    .all()
        )
    