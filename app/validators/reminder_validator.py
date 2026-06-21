from datetime import datetime
from app.models.reminder import Reminder


class ReminderValidator:
    @staticmethod
    def validate_create(reminder: Reminder) -> None:
        errors = []

        ReminderValidator._validate_common_fields(reminder, errors)

        if errors:
            raise ValueError(" | ".join(errors))

    @staticmethod
    def validate_update(reminder: Reminder) -> None:
        errors = []

        ReminderValidator._validate_common_fields(reminder, errors)

        if errors:
            raise ValueError(" | ".join(errors))

    @staticmethod
    def _validate_common_fields(reminder: Reminder, errors: list[str]) -> None:
        if reminder is None:
            errors.append("Reminder is required")
            return

        if not reminder.title or not reminder.title.strip():
            errors.append("Title is required")
        elif len(reminder.title) > 150:
            errors.append("Title must not exceed 150 characters")

        if reminder.description is not None and reminder.description.strip():
            if len(reminder.description.strip()) > 400:
                errors.append("Description must not exceed 400 characters")

        if reminder.due_date is not None and not isinstance(reminder.due_date, datetime):
            errors.append("Due date must be a valid datetime")

        if reminder.status_id is None:
            errors.append("Status is required")
        elif reminder.status_id <= 0:
            errors.append("Status must be a positive integer")

        if reminder.user_id is None:
            errors.append("User is required")
        elif reminder.user_id <= 0:
            errors.append("User must be a positive integer")

        if reminder.category_id is None:
            errors.append("Category is required")
        elif reminder.category_id <= 0:
            errors.append("Category must be a positive integer")