from fastapi import FastAPI, status
from schemas import STaskAdd, STask

app = FastAPI()


tasks = []

@app.get("/tasks", response_model=list[STask])
async def index():
    return tasks

# Создаем эндпоинт для добавления задачи
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def add_task(task: STaskAdd):
    task_dict = task.model_dump()
    task_dict["id"] = len(tasks) + 1
    tasks.append(task_dict)
    return task_dict



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9011, reload=True)
