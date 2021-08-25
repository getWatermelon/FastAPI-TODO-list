from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, Text, DateTime

from app.db.base import metadata


todos = Table(
    "todos",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("title", String(100), nullable=False),
    Column("order", Integer, nullable=False),
    Column("description", Text),
    Column("created_at", DateTime, default=datetime.now()),
    Column("updated_at", DateTime, default=datetime.now(), onupdate=datetime.now()),
)
