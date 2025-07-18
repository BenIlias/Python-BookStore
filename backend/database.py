from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_POSTGRES = 'postgresql://ilias:ilias@localhost:5433/bookstoredb'

engine = create_engine(DATABASE_POSTGRES)
LocalSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()