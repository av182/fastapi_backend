from fastapi import APIRouter, HTTPException, status
from schemas.task import STask, STaskAdd

router = APIRouter(prefix="/tasks", tags=["Задачи"])


tasks = []

@router.get("")
async def get_tasks():
    return tasks

@router.post("", response_model=STask)  
async def create_task(task: STaskAdd):
    task_dict = task.model_dump()
    task_dict["id"] = len(tasks) + 1
    tasks.append(task_dict)
    return task_dict


@router.get("/{task_id}", status_code = status.HTTP_200_OK)
async def get_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача не найдена"
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    # Используем enumerate, чтобы получить и индекс, и саму задачу
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            # Удаляем элемент списка по индексу
            tasks.pop(index)
            # Возвращаем "ничего". Это превратится в пустой ответ 204.
            return 
    
    # Если цикл прошел и ничего не нашли
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача не найдена"
    )