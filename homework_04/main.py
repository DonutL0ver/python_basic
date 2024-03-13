"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import os
from fastapi import FastAPI
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import AsyncSession, User, Post, create_tables
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd@localhost:5433/blog"
engine = create_async_engine(PG_CONN_URI)

async def add_users_to_db(users):
    async with AsyncSession() as session:
        async with session.begin():
            for user in users:
                db_user = User(name=user['name'], username=user['username'], email=user['email'])
                session.add(db_user)

async def add_posts_to_db(posts):
    async with AsyncSession() as session:
        async with session.begin():
            for post in posts:
                db_post = Post(user_id=post['userId'], title=post['title'], body=post['body'])
                session.add(db_post)

async def async_main():
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    await asyncio.gather(
        add_users_to_db(users_data),
        add_posts_to_db(posts_data)
    )

@app.on_event("startup")
async def on_startup():
    await create_tables()

if __name__ == "__main__":
    import uvicorn
    asyncio.run(async_main())
    uvicorn.run(app, host="127.0.0.1", port=8000)
