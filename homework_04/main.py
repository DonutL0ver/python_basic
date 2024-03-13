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
from sqlalchemy.orm import sessionmaker
from models import User, Post, engine, Base
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def add_users(users_data):
    Session = sessionmaker(bind=engine, async_=True, expire_on_commit=False)
    async with Session() as session:
        for user_data in users_data:
            user = User(name=user_data['name'], username=user_data['username'], email=user_data['email'])
            session.add(user)
        await session.commit()

async def add_posts(posts_data):
    Session = sessionmaker(bind=engine, async_=True, expire_on_commit=False)
    async with Session() as session:
        for post_data in posts_data:
            post = Post(user_id=post_data['userId'], title=post_data['title'], body=post_data['body'])
            session.add(post)
        await session.commit()

async def async_main():
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data()
    )

    await create_tables()
    await asyncio.gather(
        add_users(users_data),
        add_posts(posts_data)
    )

    engine.dispose()

if __name__ == '__main__':
    asyncio.run(async_main())
