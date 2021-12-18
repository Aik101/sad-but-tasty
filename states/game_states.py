from aiogram.dispatcher.filters.state import StatesGroup, State


class SinglePlayerStates(StatesGroup):
    debot_choice = State()
    dice_throwing = State()
    choice_of_winner = State()
