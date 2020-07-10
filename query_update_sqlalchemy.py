from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///users.db', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)
    location = Column('location', String)


Session = sessionmaker(bind= engine)

session = Session()

q_result = session.query(User).all() # returns a resultset inthe form of objects

for row in q_result:
    print(f"User {row.username} lives in {row.location}")

count_rows = session.query(User).count() # count method gives the count of rows this query would return
print(count_rows)

# to get a particular row in the result set
x = session.query(User).get(2)
print(f"id: {x.id}, User: {x.username}, location:{x.location}")

x.username = "harry"  # change the value of username
session.commit()  # commit the transaction

# check to see if the value is updated.
x = session.query(User).get(2)
print(f"id: {x.id}, User: {x.username}, location:{x.location}")

session.close()