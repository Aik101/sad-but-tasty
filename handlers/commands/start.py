from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.start_keyboard import get_start_keyboard
from loader import dp
# from utils import delete_first_second_messages


@dp.message_handler(commands=["start"], state=["*"])
async def command_start(message: types.Message, state: FSMContext):
    await state.reset_state(False)
    # await message.delete()
    # if not await database.get_user(message.chat.id):
    #     await database.add_user(message.chat.id, message.chat.full_name)
    keyboard = await get_start_keyboard()
    # await delete_first_second_messages(message.chat.id, await state.get_data())

    first_message = await message.answer("🤖", reply_markup=keyboard)
    second_message = await message.answer("Добро пожаловать в <b>PlayerDeBot</b>\n\n"
                                          "Здесь вы можете сыграть в кубик с настоящим децентрализованным ботом\n\n"
                                          "или же с другим человеком, но с участием дебота в качестве судьи")
    await state.update_data(first_message=first_message.message_id,
                            second_message=second_message.message_id)
