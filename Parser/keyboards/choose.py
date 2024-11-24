from aiogram.utils.keyboard import ReplyKeyboardBuilder


def choose():
    kb=ReplyKeyboardBuilder()
    kb.button(text='Погода')
    kb.button(text='Валюта')
    kb.button(text='Новости')
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)
