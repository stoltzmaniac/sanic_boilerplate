from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from my_app.models import Base, User


db_name = 'postgres://quart:quart@localhost:5432/quart'

engine = create_engine(db_name)
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
