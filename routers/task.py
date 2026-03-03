from fastapi import APIRouter, Depends
from typing import Annotated

from sqlalchemy import select

from database import SessionDep
from models.tasks import TasksModel
from schemas.task import STask, STaskAdd

router = APIRouter(prefix="/tasks", tags=["Задачи"])

@router.post("", response_model=STask)
async def create_task(
    task: STaskAdd,
    session: SessionDep
):
    # 1. Превращаем Pydantic-схему в модель БД
    # task.model_dump() вернет словарь {"name": "...", ...}
    # ** - это распаковка словаря
    new_task = TasksModel(**task.model_dump())
    
    # 2. Добавляем в сессию
    session.add(new_task)
    
    # 3. Коммитим (сохраняем на диск)
    await session.commit()
    
    # 4. Обновляем объект (получаем выданный ID)
    await session.refresh(new_task)
    
    # 5. Возвращаем объект БД. Pydantic сам превратит его в JSON.
    return new_task

@router.get("")
async def get_tasks(session: SessionDep):
    # 1. Формируем запрос
    query = select(TasksModel)
    
    # 2. Выполняем запрос
    result = await session.execute(query)
    
    # 3. Получаем чистые объекты (scalars) и превращаем в список (all)
    return result.scalars().all()