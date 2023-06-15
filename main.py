from aiogram import executor
import logging
from config import dp
from handlers import client, callback, extra, admin


client.register_client_callback(dp)
callback.register_callback(dp)
admin.register_admin(dp)

extra.register_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
