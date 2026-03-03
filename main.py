from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager
from database import engine, Model
from schemas.task import STask, STaskAdd
from routers.task import router as tasks_router
from models.tasks import TasksModel  # Нужно, чтобы таблица зарегистрировалась


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- КОД ПРИ СТАРТЕ ---
    # Мы обращаемся к движку и просим создать все таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

    print("База данных готова к работе")

    yield  # Разделяет старт и выключение

    # --- КОД ПРИ ВЫКЛЮЧЕНИИ ---
    print("Выключение сервера")


# Передаем lifespan в приложение
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=9011, reload=True)
