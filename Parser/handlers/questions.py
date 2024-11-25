from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove, FSInputFile
from Parser.handlers.screenshot import screenshot_func
from Parser.keyboards.choose import choose

router=Router()

@router.message(Command("start"))
async def start_cmd(message):
    await message.answer("Hello my friend", reply_markup=choose())

@router.message(F.text.lower() == "погода")
async def weather(message):
    await screenshot_func('weather')
    await message.answer_photo(FSInputFile('weather.png' ))

@router.message(F.text.lower() == "валюта")
async def usdt(message):
    await screenshot_func('rubus')
    await message.answer_photo(FSInputFile('rubus.png'))

@router.message(F.text.lower() == "новости")
async def news(message):
    await screenshot_func('news')
    await message.answer_photo(FSInputFile('news.png'))

