from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_POSTGRES = 'postgresql://ilias:ilias@localhost:5433/bookstoredb'

engine = create_engine(DATABASE_POSTGRES)
local_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()