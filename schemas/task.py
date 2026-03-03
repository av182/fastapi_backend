from pydantic import BaseModel, Field

class STaskAdd(BaseModel):
    name: str = Field(..., title="Название задачи", min_length=2, max_length=100)
    description: str | None = Field(None, title="Детали задачи", max_length=300)
    priority: int = Field(1, ge=1, le=5)


class STask(BaseModel):
    id: int
    name: str
    description: str
    priority: int
