import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from token import TOKEN
from Parser.handlers import questions, different


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    dp.include_routers(questions.router, different.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__=='__main__':
    asyncio.run(main())