from aiogram import Bot, Dispatcher, types

bot=Bot(token='')
dp=Dispatcher(bot)

@dp.message_reaction()