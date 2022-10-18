import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from L05.models import Base, User

engine = create_engine('sqlite:///user.db', echo=False)

# Base.mentadata.drop_all(engine)
Base.mentadata.create_all(engine)

Session =  sessionmaker(bind=engine)
session = Session()

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)
