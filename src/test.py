import os
from sqlalchemy import create_engine
from random import randint
#docker exec -it postgresql sh
#psql -U user
# \l  \dt \db  \q

NAME = os.environ.get("POSTGRES_DB"),
USER = os.environ.get("POSTGRES_USER"),
PASSWORD = os.environ.get("POSTGRES_PASSWORD"),
HOST = os.environ.get("POSTGRES_HOST"),
PORT = os.environ.get("POSTGRES_PORT")


DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{USER[0]}:{PASSWORD[0]}@{HOST[0]}:{PORT}/{NAME[0]}'
engine = create_engine(DATABASE_CONNECTION_URI)
res = engine.execute('select * from owner;')

one_owner = res.fetchone()
all_owner = res.fetchall()


print('+' * 40)
print(all_owner)
print(one_owner['name'], one_owner['addr'])
print('+' * 40)


name = "Lera" + str(randint(0, 100))
city = "Grodno" + str(randint(0, 100))

row = f"insert into owner (name, addr) values ('{name}', '{city}')"
engine.execute(row)