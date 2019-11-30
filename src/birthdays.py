from celery import Celery
from time import sleep
import os
#celery -A birthdays worker --pool=solo --loglevel=info      рабочие процессы
#celery -A birthdays beat -l info                            планировщик ритмов

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