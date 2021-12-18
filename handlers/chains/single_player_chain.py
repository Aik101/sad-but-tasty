from aiogram import types
from aiogram.dispatcher import FSMContext

from states.game_states import SinglePlayerStates
from loader import dp
from config import localhost

import subprocess


@dp.callback_query_handler(text="guess_1_callback", state=["*"])
async def confirm_person_choice_1(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>1</b>")
    await state.update_data(person_choise=1)
    await SinglePlayerStates.debot_choice.set()
    await debot_chooses(localhost, call, state)


@dp.callback_query_handler(text="guess_2_callback", state=["*"])
async def confirm_person_choice_2(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>2</b>")
    await state.update_data(person_choise=2)
    await SinglePlayerStates.debot_choice.set()
    await debot_chooses(localhost, call, state)


@dp.callback_query_handler(text="guess_3_callback", state=["*"])
async def confirm_person_choice_3(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>3</b>")
    await state.update_data(person_choise=3)
    await SinglePlayerStates.debot_choice.set()
    await debot_chooses(localhost, call, state)


@dp.callback_query_handler(text="guess_4_callback", state=["*"])
async def confirm_person_choice_4(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>4</b>")
    await state.update_data(person_choise=4)
    await SinglePlayerStates.debot_choice.set()
    await debot_chooses(localhost, call, state)


@dp.callback_query_handler(text="guess_5_callback", state=["*"])
async def confirm_person_choice_5(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>5</b>")
    await state.update_data(person_choise=5)
    await SinglePlayerStates.debot_choice.set()
    await debot_chooses(localhost, call, state)


@dp.callback_query_handler(text="guess_6_callback", state=["*"])
async def confirm_person_choice_6(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(False)
    await call.message.answer(text="Вы выбрали число <b>6</b>")
    await state.update_data(person_choise=6)
    await SinglePlayerStates.debot_choice.set()
    await debot_chooses(localhost, call, state)


async def debot_chooses(url: str, call: types.CallbackQuery, state: FSMContext):
    with open("debot/address.log") as address_file:
        debot_addr = address_file.readline()[:-1]

    command = f"./debot/tonos-cli --url {url} run --abi debot/debotPlayer.abi.json {debot_addr} guessNumber {{}}"
    res = subprocess.run(command, shell=True, capture_output=True)
    debot_choise = 0
    if len(res.stderr) != 0:
        print(res.stderr.decode('utf-8'))
    for line in res.stdout.decode('utf-8').split("\n"):
        if line.startswith('  "value0"'):
            debot_choise = int(line[13:-1], 16)
    if debot_choise == 0:
        print("invalid debot choice")

    await state.update_data(debot_choise=debot_choise)
    await call.message.answer(text=f"ДеБот выбрал число <b>{debot_choise}</b>")
