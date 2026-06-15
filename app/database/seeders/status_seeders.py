from app.models.status import Status

def seed_status(db):
    
    statuses = [
        {'title' : 'Pending','description' : '...'},
        {'title' : 'Completed','description' : '...'},
        {'title' : 'Overdue','description' : '...'},
        {'title' : 'Deleted','description' : '...'},
    ]
    
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