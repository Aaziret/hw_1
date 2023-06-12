from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from decouple import config
import logging

TOKEN = '6190010458:AAHnm15T6zyfmBd9WVy4uXS8suFbeD47b5g'
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "сколько хокаге в деревне скрытого листа"
    answers = [
        "7",
        "8",
        "2",
        "4",
        "3",
        "5",
    ]


    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="ты не смотрел наруто?",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
    quiestion = "Сколько лет Geeks?"
    answers = [
        "2 года",
        "что это?",
        "3 года ",
        "5 лет",
        "год",
    ]

    
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Серьезно?",
        open_period=10, )


@dp.message_handler(commands=['mem'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEJSiVkhvp2J3FCtFGOIZaR9J-JH57POwACbw4AAjbjkUuGuF6BDebzkS8E", )


@dp.message_handler(commands=['mems'])
async def start_command_1(message: types.Message):
    photo = open('media/detail_dad9dde83048e2a200dfecf4355dbc5e.jpg', 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler()
async def hendler_echo(message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)


logging.basicConfig(level=logging.INFO)
executor.start_polling(dp, skip_updates=True)
