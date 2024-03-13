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
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post, Base
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def create_tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_users(engine, users_data):
    async_session = sessionmaker(engine, class_=AsyncSession)
    async with async_session() as session:
        for user_data in users_data:
            user = User(name=user_data['name'], username=user_data['username'], email=user_data['email'])
            session.add(user)
        await session.commit()


async def add_posts(engine, posts_data):
    async_session = sessionmaker(engine, class_=AsyncSession)
    async with async_session() as session:
        for post_data in posts_data:
            post = Post(user_id=post_data['userId'], title=post_data['title'], body=post_data['body'])
            session.add(post)
        await session.commit()


async def async_main():
    database_url = 'sqlite+aiosqlite:///./data.db'
    engine = create_async_engine(database_url, echo=True)

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data()
    )

    await create_tables(engine)
    await asyncio.gather(
        add_users(engine, users_data),
        add_posts(engine, posts_data)
    )


if __name__ == 'main':
    asyncio.run(async_main())
