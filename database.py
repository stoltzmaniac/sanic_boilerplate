from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
from my_app.models import Base, User


db_name = Config.DATABASE_URI

engine = create_engine(db_name)
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
