from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
# secrets = json.loads(open(SECRET_FILE).read())
# DB = secrets["DB"]

# DB_URL = f"mysql+pymsql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

DB_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    # DB_URL, encoding = 'utf-8'
    DB_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

