from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, Integer
from app.database.database import Base

class Status(Base):
    
    __tablename__ = 'statuses'
    
    status_id : Mapped[int] = mapped_column(
        Integer,
        primary_key = True
    )
    
    title: Mapped[str] = mapped_column(
        String(50)
    )
    
    description: Mapped[str] = mapped_column(
        String(150)
    )
    
    reminders = relationship(
        'Reminder',
        back_populates= 'status'
    )
    
    