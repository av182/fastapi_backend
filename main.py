from fastapi import FastAPI, HTTPException, status
from schemas.task import STask, STaskAdd
from routers.task import router as tasks_router

app = FastAPI()

# Подключаем роутер к приложению
app.include_router(tasks_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9011, reload=True)
