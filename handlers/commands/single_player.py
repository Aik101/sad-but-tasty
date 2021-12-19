from aiogram import types
from aiogram.dispatcher import FSMContext

from states.game_states import SinglePlayerStates
from keyboards.guess_number_keyboard import get_guess_number_keyboard
from loader import dp


@dp.message_handler(text=["🤖 Играть с ДеБотом"], state=["*"])
async def start_single_player(message: types.Message, state: FSMContext):
    await state.reset_state(False)
    await message.delete()
    keyboard = await get_guess_number_keyboard()

    await SinglePlayerStates.person_choice.set()
    first_message = await message.answer("🤔")
    second_message = await message.answer("Предположите число, которое выпадет на кубике\n\n"
                                          "<b>Выберите число ⤵️</b>",
                                          reply_markup=keyboard)

    await state.update_data(messages_two={0: first_message.message_id, 1: second_message.message_id})
