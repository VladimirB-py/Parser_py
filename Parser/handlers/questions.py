from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import FSInputFile
from Parser.handlers.screenshot import screenshot_func
from Parser.keyboards.choose import choose
from Parser.fetch import dollar, news_list

offset=0
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
    await message.answer(f"За 1 долляр в втб получишь - {dollar.json()['toSumma']} руб")

@router.message(F.text.lower() == "новости")
async def news(message):
    end = 8
    global offset
    for element in news_list[offset: offset + end]:
        await message.answer(element)
    offset += end