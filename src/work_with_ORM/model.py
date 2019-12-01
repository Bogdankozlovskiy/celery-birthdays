from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from connect import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'my_user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    addresses = relationship("Address", backref="my_user",
                             order_by="Address.id")


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('my_user.id'))
    email_address = Column(String)


Base.metadata.create_all(engine)
