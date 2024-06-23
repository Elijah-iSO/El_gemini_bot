import asyncio

from aiogram import Bot, Dispatcher

from app.handlers import router
from config import B_TOKEN


async def main():
    bot = Bot(token=B_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
