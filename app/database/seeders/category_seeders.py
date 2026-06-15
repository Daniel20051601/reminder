from app.models.category import Category

def seed_categories(db):
    
    categories = [
        {'title' : 'Personal',
         'description' : '...'},
        {'title' : 'Study',
         'description' : '...'},
        {'title' : 'Work',
         'description' : '...'},
        {'title' : 'Health',
         'description' : '...'},
        {'title' : 'Finance',
         'description' : '...'}
    ]
    
    for category in categories:
         
         exists = (db.query(Category)
                    .filter(
                        Category.title == category['title']
                    )
                    .first()
        )
         
         if not exists:
             db.add(
                 Category(
                     title = category['title'],
                     description = category['description']
                 )
             )
             
    db.commit()