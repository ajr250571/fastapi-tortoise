# models.py
from datetime import datetime
from pony.orm import Required, Optional, Set, PrimaryKey
from config import db


class User(db.Entity):
    _table_ = 'users'
    id = PrimaryKey(int, auto=True)
    username = Required(str, unique=True)
    email = Required(str, unique=True)
    created_at = Required(datetime, default=datetime.now)
    posts = Set('Post')


class Post(db.Entity):
    _table_ = 'posts'
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    content = Required(str)
    created_at = Required(datetime, default=datetime.now)
    author = Required(User)


db.generate_mapping(create_tables=True)
