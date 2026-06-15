from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, ForeignKey, func, DateTime, Integer
from app.database.database import Base
from datetime import datetime

class Reminder(Base):
    
    __tablename__ = 'reminders'
    
    reminder_id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    
    title: Mapped[str] = mapped_column(
        String(150)
    )
    
    description: Mapped[str] = mapped_column(
        String(400)
    )
    
    created_date: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )
    
    due_date: Mapped[datetime | None ] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    
    status_id : Mapped[int] = mapped_column(
        ForeignKey('statuses.status_id')
    )
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.user_id')
    )
    
    category_id : Mapped[int] = mapped_column(
        ForeignKey('categories.category_id')
    )
    
    status = relationship(
        'Status',
        back_populates='reminders'
    )
    
    users = relationship(
        'User',
        back_populates = 'reminders'
    )
    
    categories = relationship(
        'Category',
        back_populates= 'reminders'
    )
    
    