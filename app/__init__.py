from fastapi import FastAPI
from app.db import database

from app.api.routes import todo

app = FastAPI(
    title=f"TODO-list Rest API",
    description=f"Simple API for TODO-list",
)

app.include_router(todo.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
