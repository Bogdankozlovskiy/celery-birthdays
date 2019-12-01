import os
from sqlalchemy import create_engine


NAME = os.environ.get("POSTGRES_DB")
USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
HOST = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")


DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'
engine = create_engine(DATABASE_CONNECTION_URI)