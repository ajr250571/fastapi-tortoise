# config.py
from pony.orm import Database
from dotenv import load_dotenv
import os

load_dotenv()

db = Database()
db.bind(provider='mysql',
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        passwd=os.getenv('DB_PASSWORD', ''),
        db=os.getenv('DB_NAME', 'pony-db'))
