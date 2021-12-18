from aiogram.utils.executor import start_polling
# from utils.database_api.main import init_db


# async def on_start(dp):
#     await init_db()


if __name__ == '__main__':
    from handlers import dp

    start_polling(dp)
