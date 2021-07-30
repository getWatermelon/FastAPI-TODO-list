from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: int
    title: str
    order: int
    description: Optional[str]
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()


class TodoIn(BaseModel):
    title: str = Field(..., min_length=1,
                       description="title length must be at least 1 character")
    order: int = Field(..., gt=0, lt=1000,
                       description="Task order number must be more than 0 and less than 1000")
    description: Optional[str]
