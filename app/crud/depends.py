from app.db import database
from app.crud import CRUDTodo


def get_database() -> CRUDTodo:
    return CRUDTodo(database)
