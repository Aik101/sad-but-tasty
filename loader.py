from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import bot_token
# from utils.database_api.commands.main import DB_Commands

bot = Bot(bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
# database = DB_Commands()
