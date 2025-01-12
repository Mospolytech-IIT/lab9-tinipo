from fastapi import FastAPI
from app.routers import users, posts
from app.database import init_db

app = FastAPI(title="FastAPI with PostgreSQL")

# Подключение маршрутов
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])

@app.on_event("startup")
async def on_startup():
    # Инициализация базы данных
    await init_db()

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with PostgreSQL!"}
