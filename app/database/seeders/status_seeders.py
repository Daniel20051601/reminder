from app.models.status import Status
from app.resources.text.seed_data import STATUSES

def seed_status(db):
    
    statuses = STATUSES
    
    for status in statuses:
        
        exits = (
            db.query(Status)
                .filter(
                    Status.title == status['title']
                )
                .first()
        )
        
        if not exits:
            db.add(
                Status(
                    title = status['title'],
                    description = status['description']
                )
            )
    
    db.commit()