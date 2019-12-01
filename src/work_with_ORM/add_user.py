from model import User, Address
from connect import engine
from sqlalchemy.orm import Session


session = Session(bind=engine)



address1 = Address(email_address="vas@example.com")
address2 = Address(email_address="vas2@example.com")
address3 = Address(email_address="vasya@example.com")

user1 = User(name="Вася")
user1.addresses = [address1, address2, address3]

session.add(user1)



session.commit()