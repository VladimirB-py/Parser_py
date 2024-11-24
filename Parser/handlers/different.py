from aiogram import F, Router


router= Router()

@router.message(F.text)
async def message_with_text(message):
    await message.answer('text message')

@router.message(F.sticker)
async def message_with_sticker(message):
    await message.answer('sticker attach')

@router.message(F.animation)
async def message_with_gif(message):
    await message.answer('GIF detected')