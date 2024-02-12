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
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import engine, AsyncSessionLocal, User, Post, Base
from fastapi import FastAPI

async def async_main():
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    await asyncio.gather(
        add_users_to_db(users_data),
        add_posts_to_db(posts_data)
    )

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def add_users_to_db(users):
    async with AsyncSessionLocal() as session:
        async with session.begin():
            for user in users:
                db_user = User(name=user['name'], username=user['username'], email=user['email'])
                session.add(db_user)

async def add_posts_to_db(posts):
    async with AsyncSessionLocal() as session:
        async with session.begin():
            for post in posts:
                db_post = Post(user_id=post['userId'], title=post['title'], body=post['body'])
                session.add(db_post)

if __name__ == "__main__":
    asyncio.run(async_main())

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await create_tables()
    if __name__ == "__main__":
        asyncio.run(async_main())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
