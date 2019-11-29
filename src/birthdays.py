from celery import Celery
from time import sleep
from psycopg2 import connect
import os
#celery -A birthdays worker --pool=solo --loglevel=info      рабочие процессы
#celery -A birthdays beat -l info                            планировщик ритмов

NAME = os.environ.get("DB_NAME")
USER = os.environ.get("DB_USER")
PASSWORD = os.environ.get("PGPASSWORD")
HOST = os.environ.get("DB_HOST")
PORT = os.environ.get("DB_PORT")

print('*' * 25)
print(NAME, USER, PASSWORD, HOST, PORT)
print('*' * 25)
conn = connect(
	host = HOST,
	port = PORT,
	database = NAME,
	user = USER,
	password = PASSWORD
	)

app = Celery(
    'birthdays', 
    broker = 'redis://redis:6379/0'
    )

app.conf.update(
    result_backend = 'redis://redis:6379/0'
    )

@app.task
def birthdays_today():
    return 'hello world matherfucker!'


#add "birthdays_today" task to the beat schedule
app.conf.beat_schedule = {
    "birthday-task": {
        "task": "birthdays.birthdays_today",
        "schedule": 30.0,
   }
}