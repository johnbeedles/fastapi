from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Use 'psycopg' instead of 'psycopg2'
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# used before we used SQLAlchemy
# import psycopg
# import time
# from psycopg.rows import dict_row
# connect to database, if table doesn't exist create it
# while True:
#     try:
#         # Update psycopg connection
#         conn = psycopg.connect(
#             host="localhost",
#             dbname="fastapi",
#             user="postgres",
#             password="Cl1pW1ng",
#             row_factory=dict_row
#         )
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print(f"Connection Failed.\nError: {error}")
#         time.sleep(3)
