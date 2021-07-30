from app.db.models import todos
from app.db.base import (
    metadata,
    engine,
    database
)

metadata.create_all(bind=engine)
