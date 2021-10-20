from aiogram import Bot, Dispatcher, executor
from cripto.settings import BOT_TOKEN
import asyncio

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from cripto.handlers import dp, send_start_to_admin, send_shutdown_to_admin
    # executor.start_polling(dp, on_startup=send_start_to_admin, on_shutdown=send_shutdown_to_admin)
    executor.start_polling(dp)



