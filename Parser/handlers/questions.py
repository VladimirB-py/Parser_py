from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove

from Parser.keyboards.choose import choose

router=Router()

@router.message(Command("start"))
async def start_cmd(message):
    await message.answer("Hello my friend", reply_markup=choose())

@router.message(F.text.lower() == "погода")
async def weather(message):
    await message.answer("The Weather is like today", reply_markup=ReplyKeyboardRemove())

@router.message(F.text.lower() == "валюта")
async def usdt(message):
    await message.answer("MoneyMoneyMoney", reply_markup=ReplyKeyboardRemove())

@router.message(F.text.lower() == "новости")
async def news(message):
    await message.answer("In Bogdad is very good", reply_markup=ReplyKeyboardRemove())