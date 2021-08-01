from typing import List, Union
from datetime import datetime

from sqlalchemy import asc, desc

from app.db import todos
from app.crud.base import CRUDDatabase
from app.schemas import Todo, TodoIn


class CRUDTodo(CRUDDatabase):

    async def get_all(self) -> List[Todo]:
        query = (todos.select()
                 .order_by(
                    asc(todos.c.order),
                    desc(todos.c.updated_at))
                 .limit(100))

        todos_list = [Todo(**todo) for todo in await self.database.fetch_all(query=query)]

        return todos_list

    async def get_one_by_id(self, id: int) -> Union[Todo, None]:
        query = (todos.select()
                 .where(todos.c.id == id))

        todo = await self.database.fetch_one(query=query)
        if not todo:
            return None

        return Todo(**todo)

    async def create(self, todo: TodoIn) -> Todo:
        current_time = datetime.now()

        new_todo = dict(
            title=todo.title,
            order=todo.order,
            description=todo.description,
            created_at=current_time,
            updated_at=current_time
        )

        query = todos.insert().values(**new_todo)

        todo_id = await self.database.execute(query=query)

        return Todo(**dict(id=todo_id, **new_todo))

    async def update(self, id: int, todo_in: TodoIn, edited_todo: Todo) -> Todo:
        update_time = datetime.now()

        todo = dict(
            title=todo_in.title,
            order=todo_in.order,
            description=todo_in.description,
            updated_at=update_time
        )

        query = (todos.update()
                 .where(todos.c.id == id)
                 .values(**todo))

        await self.database.fetch_one(query=query)

        return Todo(**dict(**todo, id=id, created_at=edited_todo.created_at))

    async def delete(self, id: int) -> None:
        query = todos.delete(todos.c.id == id)

        await self.database.execute(query=query)
        return None
