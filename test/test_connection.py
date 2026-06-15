import sys
import os
sys.path.append(os.path.abspath(".."))
from app.database.session import SessionLocal

db = SessionLocal()

try:
    print("Connected successfully!")
finally:
    db.close()