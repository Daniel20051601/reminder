from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

class User(Base):
    
    __tablename__ = 'users'
    
    user_id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    
    name : Mapped[str] = mapped_column(
        String(150)
    )
    
    token : Mapped[str] = mapped_column(
        String(100)
    )
    
    reminders = relationship(
        'Reminder',
        back_populates='users'
    )