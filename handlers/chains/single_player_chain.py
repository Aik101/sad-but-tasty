from aiogram import types
from aiogram.dispatcher import FSMContext

from states.game_states import SinglePlayerStates
from loader import dp


@dp.callback_query_handler(text="guess_1_callback", state=["*"])
async def confirm_person_choice_1(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>1</b>")
    await state.update_data(person_choise=1)
    await SinglePlayerStates.debot_choice.set()


@dp.callback_query_handler(text="guess_2_callback", state=["*"])
async def confirm_person_choice_2(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>2</b>")
    await state.update_data(person_choise=2)
    await SinglePlayerStates.debot_choice.set()


@dp.callback_query_handler(text="guess_3_callback", state=["*"])
async def confirm_person_choice_3(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>3</b>")
    await state.update_data(person_choise=3)
    await SinglePlayerStates.debot_choice.set()


@dp.callback_query_handler(text="guess_4_callback", state=["*"])
async def confirm_person_choice_4(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>4</b>")
    await state.update_data(person_choise=4)
    await SinglePlayerStates.debot_choice.set()


@dp.callback_query_handler(text="guess_5_callback", state=["*"])
async def confirm_person_choice_5(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>5</b>")
    await state.update_data(person_choise=5)
    await SinglePlayerStates.debot_choice.set()


@dp.callback_query_handler(text="guess_6_callback", state=["*"])
async def confirm_person_choice_6(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>6</b>")
    await state.update_data(person_choise=6)
    await SinglePlayerStates.debot_choice.set()
