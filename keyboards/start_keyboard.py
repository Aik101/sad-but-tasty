from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        KeyboardButton("🤖 Играть с ДеБотом"),
        KeyboardButton("🤠 Играть с человеком")
    )
    return keyboard
