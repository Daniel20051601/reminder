from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base


class Category(Base):
    
    __tablename__ = 'categories'
    
    category_id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    
    title: Mapped[str] = mapped_column(
        String(150)
    )
    
    description : Mapped[str] = mapped_column(
        String(400)
    )
    
    reminders = relationship(
        'Reminder',
        back_populates='categories'
    )