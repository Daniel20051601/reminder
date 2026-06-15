from app.models.category import Category
from app.resources.text.seed_data import CATEGORIES

def seed_categories(db):
    
    categories = CATEGORIES
    
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