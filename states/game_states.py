from aiogram.dispatcher.filters.state import StatesGroup, State


class SinglePlayerStates(StatesGroup):
    person_choice = State()
    debot_choice = State()
    dice_throwing = State()
    choice_of_winner = State()


class MultiPlayerStates(StatesGroup):
    person_1_choice = State()
    person_2_choice = State()
    dice_throwing = State()
    choice_of_winner = State()
