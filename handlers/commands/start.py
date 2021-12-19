from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.start_keyboard import get_start_keyboard
from loader import dp
from utils.interface_utils import delete_2_messages


@dp.message_handler(commands=["start"], state=["*"])
async def command_start(message: types.Message, state: FSMContext):
    await state.reset_state(False)
    await message.delete()
    keyboard = await get_start_keyboard()
    first_message = await message.answer("🤖", reply_markup=keyboard)
    second_message = await message.answer("Добро пожаловать в <b>PlayerDeBot</b>\n\n"
                                          "Здесь вы можете сыграть в кубик с настоящим "
                                          "децентрализованным ботом блокчейна Everscale\n\n"
                                          "Или же с другим человеком, но с участием ДеБота в качестве судьи")

    await state.update_data(messages_two={0: first_message.message_id, 1: second_message.message_id})
