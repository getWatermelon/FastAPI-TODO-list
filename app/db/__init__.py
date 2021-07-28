from .base import (
    metadata,
    engine,
    database
)

metadata.create_all(bind=engine)
