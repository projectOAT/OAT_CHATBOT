# database.py

from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
import config

# Database URI
DB_URI = f"mysql+pymysql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}"

# Connect to MySQL Database
def get_database():
    return SQLDatabase.from_uri(DB_URI)

db = get_database()
