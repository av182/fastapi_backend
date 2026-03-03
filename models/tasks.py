from sqlalchemy.orm import Mapped, mapped_column
from database import Model

class TasksModel(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]
    description: Mapped[str | None]
    priority: Mapped[int]
    # Добавляем новое поле (по умолчанию False, если не указано иное)
    # Но в БД лучше явно требовать значение, а дефолты ставить в Pydantic
    is_completed: Mapped[bool] = mapped_column(default=False)