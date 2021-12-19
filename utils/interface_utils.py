from typing import Dict

from loader import dp


async def delete_2_messages(user_id, data: Dict):
    for i in range(2):
        try:
            await dp.bot.delete_message(user_id, data['messages_two'].get(i))
        except Exception:
            pass
