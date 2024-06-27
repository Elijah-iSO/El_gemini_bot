import aiohttp
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

from app.database.models import async_main
from app.handlers import router
from config import TOKEN

proxy = 'http://161.34.39.156:3128'
session = AiohttpSession(proxy=proxy)


async def main():
    bot = Bot(token=TOKEN, session=session)
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


async def on_startup(dispatcher):
    await async_main()


async def test_proxy(proxy):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.ipify.org?format=json', proxy=proxy) as resp:
            print(await resp.json())


if __name__ == '__main__':
    try:
        asyncio.run(main())
        asyncio.run(test_proxy(proxy))
    except KeyboardInterrupt:
        pass
