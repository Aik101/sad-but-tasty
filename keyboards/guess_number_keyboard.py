from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_guess_number_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("1️⃣", callback_data="guess_1_callback"),
        InlineKeyboardButton("2️⃣", callback_data="guess_2_callback"),
        InlineKeyboardButton("3️⃣", callback_data="guess_3_callback"),
        InlineKeyboardButton("4️⃣", callback_data="guess_4_callback"),
        InlineKeyboardButton("5️⃣", callback_data="guess_5_callback"),
        InlineKeyboardButton("6️⃣", callback_data="guess_6_callback"),
    )
    return keyboard
