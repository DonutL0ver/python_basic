import asyncio
from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from homework_04.myenv.DB import create_tables, add_users_to_db, add_posts_to_db


async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data()
    )
    await asyncio.gather(
        add_users_to_db(users_data),
        add_posts_to_db(posts_data)
    )

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
