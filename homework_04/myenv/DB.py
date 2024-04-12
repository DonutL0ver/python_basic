from homework_04.main import async_session, engine, Base
from homework_04.models import User, Post


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def add_users_to_db(users_data):
    async with async_session() as session:
        session.add_all([User(**user) for user in users_data])
        await session.commit()

async def add_posts_to_db(posts_data):
    async with async_session() as session:
        session.add_all([Post(**post) for post in posts_data])
        await session.commit()
