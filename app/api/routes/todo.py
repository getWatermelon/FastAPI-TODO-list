from typing import List

from starlette import status
from fastapi import Depends, HTTPException, APIRouter

from app.schemas import Todo, TodoIn
from app.crud.depends import get_database
from app.crud import CRUDTodo

router = APIRouter()


@router.get("/todos/", response_model=List[Todo], status_code=status.HTTP_200_OK, tags=["TODO"])
async def get_all_todos(todos: CRUDTodo = Depends(get_database)):
    return await todos.get_all()


@router.get("/todo/{id}", response_model=Todo, status_code=status.HTTP_200_OK, tags=["TODO"])
async def get_todo_by_id(id: int, todos: CRUDTodo = Depends(get_database)):
    todo = await todos.get_one_by_id(id)

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TODO-list Item with id = {id} Not Found"
        )

    return todo


@router.post("/todo/create", response_model=Todo, status_code=status.HTTP_201_CREATED, tags=["TODO"])
async def create_todo(todo: TodoIn, todos: CRUDTodo = Depends(get_database)):
    return await todos.create(todo)


@router.put("/todo/{id}/edit", response_model=Todo, status_code=status.HTTP_200_OK, tags=["TODO"])
async def update_todo(id: int, todo_in: TodoIn, todos: CRUDTodo = Depends(get_database)):
    edited_todo = await todos.get_one_by_id(id)
    if not edited_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TODO-list Item with id = {id} Not Found"
        )

    return await todos.update(id, todo_in, edited_todo)


@router.delete("/todo/{id}/delete", status_code=status.HTTP_204_NO_CONTENT, tags=["TODO"])
async def delete_todo(id: int, todos: CRUDTodo = Depends(get_database)):
    if not await todos.get_one_by_id(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TODO-list Item with id = {id} Not Found"
        )

    return await todos.delete(id)
