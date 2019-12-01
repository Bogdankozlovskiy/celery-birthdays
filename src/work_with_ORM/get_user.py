from model import User, Address
from sqlalchemy.orm import Session
from connect import engine
from sqlalchemy import select


session = Session(bind=engine)
query = session.query(User).order_by(User.id)



for user in query.all():
	print(user.name)
	sel = select([Address.email_address]).where(Address.user_id == user.id).order_by(Address.id)
	for em in session.connection().execute(sel).fetchall():
		print(*em)