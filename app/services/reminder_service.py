from app.models.reminder import Reminder
from app.repositories.reminder_repository import ReminderRepository
from app.validators.reminder_validator import ReminderValidator

class ReminderService:
    def __init__(self, reminder_repository: ReminderRepository):
        self.reminder_repository = reminder_repository
        
    def create_reminder(self, reminder: Reminder) -> Reminder:
            ReminderValidator.validate_create(reminder)

            try:
                return  self.reminder_repository.create(reminder)
            except Exception as error:
                raise RuntimeError(
                    'Could not create reminder'
                )from error
    
    def get_reminder(self, reminder_id: int) -> Reminder:
        reminder = self.reminder_repository.get_by_id(reminder_id)
        
        if not reminder:
            raise ValueError(
                'Reminder not found'
            )
        
        return reminder
    
    def get_reminders(self) -> list[Reminder]:
        return self.reminder_repository.get_all()
    
    def update_reminder(self, reminder_id: int, reminder: Reminder) -> Reminder:
        ReminderValidator.validate_update(reminder)
        
        reminder_to_update = self.get_reminder(reminder_id)

        reminder_to_update.title = reminder.title
        reminder_to_update.description = reminder.description
        reminder_to_update.due_date = reminder.due_date
        reminder_to_update.status_id = reminder.status_id
        reminder_to_update.category_id = reminder.category_id

        return self.reminder_repository.update(reminder_to_update)
        
        
    def delete_reminder(self, reminder_id: int) -> Reminder:
        reminder = self.get_reminder(reminder_id)
        
        if not reminder:
            raise ValueError(
                'Reminder not found'
            )
        
        return self.reminder_repository.delete(reminder)
    
    def get_reminders_by_category(self, category_id: int) -> list[Reminder]:
        return self.reminder_repository.reminders_by_category(category_id)
    
    def get_completed_reminders(self) -> list[Reminder]:
        return self.reminder_repository.get_completed_reminders()
    
    def mark_reminder(self, reminder_id: int) -> Reminder:
        reminder = self.get_reminder(reminder_id)
        
        if not reminder:
            raise ValueError(
                "Reminder not found"
            )
        
        return self.reminder_repository.mark_reminder(reminder)
        