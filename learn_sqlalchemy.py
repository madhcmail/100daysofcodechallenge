from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer,String, create_engine

# declarative_base is a Factory function used to create a Base class which contains catlog of classes and mapped tables
# once Base class is defined any number of mapped classes can be defined.
Base = declarative_base()


class User(Base):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)
    location = Column('location', String)

# creating the Sqlite engine and creating the db and table under it
engine = create_engine('sqlite:///users.db', echo=True)

# each Table object is a member of larger collection Knows as MetaData and the object is available using .metadata atrribute of
# declarative base class
Base.metadata.create_all(bind=engine)

# In order to interact with database, we need to obtain its handle. A session object is the handle to the database. it's
# just like a cursor that we create to parse the database in sqlite3.
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

user_1 = User()
user_1.id = 1
user_1.username = 'Scott'
user_1.location = 'NJ'

user_2 = User()
user_2.id = 2
user_2.username = 'Bob'
user_2.location = 'WA'

session.add(user_1)
session.add(user_2)

session.commit()
session.close()