from aiogram import types
from aiogram.dispatcher import FSMContext

from states.game_states import MultiPlayerStates
from loader import dp
from config import localhost
from utils.interface_utils import delete_2_messages
from keyboards.guess_number_keyboard import get_guess_number_keyboard
from keyboards.start_keyboard import get_start_keyboard
from handlers.commands.multi_player import start_multi_player
from config import localhost

import subprocess
import time


@dp.callback_query_handler(text="guess_1_callback", state=[MultiPlayerStates.person_1_choice])
async def confirm_person_1_choice_1(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Первый игрок выбрал число <b>1</b>")

    await state.update_data(person_1_choice=1)
    await start_choose_person_2(call.message, state)


@dp.callback_query_handler(text="guess_1_callback", state=[MultiPlayerStates.person_2_choice])
async def confirm_person_2_choice_1(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Второй игрок выбрал число <b>1</b>")

    await state.update_data(person_2_choice=1)
    await MultiPlayerStates.dice_throwing.set()
    await throw_dice(call, state)


@dp.callback_query_handler(text="guess_2_callback", state=[MultiPlayerStates.person_1_choice])
async def confirm_person_1_choice_2(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Первый игрок выбрал число <b>2</b>")

    await state.update_data(person_1_choice=2)
    await start_choose_person_2(call.message, state)


@dp.callback_query_handler(text="guess_2_callback", state=[MultiPlayerStates.person_2_choice])
async def confirm_person_2_choice_2(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Второй игрок выбрал число <b>2</b>")

    await state.update_data(person_2_choice=2)
    await MultiPlayerStates.dice_throwing.set()
    await throw_dice(call, state)


@dp.callback_query_handler(text="guess_3_callback", state=[MultiPlayerStates.person_1_choice])
async def confirm_person_1_choice_3(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Первый игрок выбрал число <b>3</b>")

    await state.update_data(person_1_choice=3)
    await start_choose_person_2(call.message, state)


@dp.callback_query_handler(text="guess_3_callback", state=[MultiPlayerStates.person_2_choice])
async def confirm_person_2_choice_3(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Второй игрок выбрал число <b>3</b>")

    await state.update_data(person_2_choice=3)
    await MultiPlayerStates.dice_throwing.set()
    await throw_dice(call, state)


@dp.callback_query_handler(text="guess_4_callback", state=[MultiPlayerStates.person_1_choice])
async def confirm_person_1_choice_4(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Первый игрок выбрал число <b>4</b>")

    await state.update_data(person_1_choice=4)
    await start_choose_person_2(call.message, state)


@dp.callback_query_handler(text="guess_4_callback", state=[MultiPlayerStates.person_2_choice])
async def confirm_person_2_choice_4(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Второй игрок выбрал число <b>4</b>")

    await state.update_data(person_2_choice=4)
    await MultiPlayerStates.dice_throwing.set()
    await throw_dice(call, state)


@dp.callback_query_handler(text="guess_5_callback", state=[MultiPlayerStates.person_1_choice])
async def confirm_person_1_choice_5(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Первый игрок выбрал число <b>5</b>")

    await state.update_data(person_1_choice=5)
    await start_choose_person_2(call.message, state)


@dp.callback_query_handler(text="guess_5_callback", state=[MultiPlayerStates.person_2_choice])
async def confirm_person_2_choice_5(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Второй игрок выбрал число <b>5</b>")

    await state.update_data(person_2_choice=5)
    await MultiPlayerStates.dice_throwing.set()
    await throw_dice(call, state)


@dp.callback_query_handler(text="guess_6_callback", state=[MultiPlayerStates.person_1_choice])
async def confirm_person_1_choice_6(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Первый игрок выбрал число <b>6</b>")

    await state.update_data(person_1_choice=6)
    await start_choose_person_2(call.message, state)


@dp.callback_query_handler(text="guess_6_callback", state=[MultiPlayerStates.person_2_choice])
async def confirm_person_2_choice_6(call: types.CallbackQuery, state: FSMContext):
    await delete_2_messages(call.message.chat.id, await state.get_data())
    await call.message.answer(text="Второй игрок выбрал число <b>6</b>")

    await state.update_data(person_2_choice=6)
    await MultiPlayerStates.dice_throwing.set()
    await throw_dice(call, state)


async def start_choose_person_2(message: types.Message, state: FSMContext):
    keyboard = await get_guess_number_keyboard()
    first_message = await message.answer("🤔")
    second_message = await message.answer("Предположите число, которое выпадет на кубике\n\n"
                                          "<b>Выберите число ⤵️</b>",
                                          reply_markup=keyboard)
    await MultiPlayerStates.person_2_choice.set()
    await state.update_data(messages_two={0: first_message.message_id, 1: second_message.message_id})


async def throw_dice(call: types.CallbackQuery, state: FSMContext):
    dice_res = await call.message.answer_dice(emoji="🎲")
    await state.update_data(dice_res=dice_res.dice.value)
    time.sleep(4)
    await call.message.answer(text=f"Результат <b>{dice_res.dice.value}</b>")
    await MultiPlayerStates.choice_of_winner.set()
    await compute_winner(localhost, call, state)


async def compute_winner(url: str, call: types.CallbackQuery, state: FSMContext):
    results = await state.get_data()
    diff_1_person = abs(results.get('dice_res') - results.get('person_1_choice'))
    diff_2_person = abs(results.get('dice_res') - results.get('person_2_choice'))

    with open("debot/address.log") as address_file:
        debot_addr = address_file.readline()[:-1]

    debot_decision = 0
    command = f"""./debot/tonos-cli --url {url} run --abi debot/debotPlayer.abi.json {debot_addr} compareResults '{{"a":{diff_1_person}, "b":{diff_2_person}}}'"""
    res = subprocess.run(command, shell=True, capture_output=True)
    if len(res.stderr) != 0:
        print(res.stderr.decode('utf-8'))
    for line in res.stdout.decode('utf-8').split("\n"):
        if line.startswith('  "value0"'):
            debot_decision = int(line[13:-1])

    if debot_decision == 1:
        answer = {1: "🤠", 2: f"Победил второй игрок!"}
    elif debot_decision == -1:
        answer = {1: "😈", 2: f"Победил первый игрок!"}
    else:
        answer = {1: "🗿", 2: f"Ничья!"}

    keyboard = await get_start_keyboard()
    await call.message.answer(text=answer.get(1), reply_markup=keyboard)
    await call.message.answer(text=answer.get(2))