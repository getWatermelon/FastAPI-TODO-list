from datetime import datetime
from app.db import metadata
from sqlalchemy import (
    Table, Column,
    Integer, String, Text, DateTime
)


todo_model = Table(
    'todo',
    metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('title', String(256), nullable=False),
    Column('order', Integer, nullable=False),
    Column('description', Text),
    Column('created_at', DateTime, default=datetime.now()),
    Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now())
)
