from aiogram import Bot, Dispatcher, F
from aiogram.filters import Text, Command
from aiogram.types import Message, InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

import os
from dotenv import load_dotenv

from parse_product import Parser
from utils import make_product_message


load_dotenv()
API_TOKEN: str = os.getenv('API_TOKEN')

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

#хэндлер на '/start' и '/help'
@dp.message(Command(commands=['start']))
@dp.message(Command(commands=['help']))
async def start_command(message: Message):
    await message.answer('Привет!\nЯ - бот, созданный для поиска косметики/парфюма, сравнения цены продукта на разных площадках и быстрого доступа к отзывам\n\nЧтобы начать, отправь мне название продукта!\n\n! Пожалуйста, указывайте конкретный продукт в запросе! Чем точнее Ваш запрос, тем больше вероятность найти продукт\n\nПримеры хороших запросов:\nDIOR ADDICT LIPSTICK\nLoreal alliance perfect nude\nVivienne Sabo Gloire Damour\nLoreal alliance perfect nude\n\nПримеры плохих запросов:\nпарфюм\nDIOR LIPSTICK\nVIVIENNE SABO\nFIT ME\n\nЛюбые вопросы/предложения к @ywuqiwo')

@dp.message(F.text)
async def search(message: Message):
    query = message.text.replace('"', ' ').replace("'", ' ')

    parse = Parser(query)

    parse.parse_ga()
    try:
        parse.parse_letual()
    except:
        ...
    parse.parse_rivgauche()
    parse.parse_irecommend()

    ans = make_product_message(query, parse.product.get_product(), parse.product.get_product_rating())

    if parse.product.get_product_photo() is not None:
        photo = parse.product.get_product_photo()
    else:
        photo = FSInputFile('sadcat.jpg')

    if parse.product.get_product_reviews_link() is not None:
        builder = InlineKeyboardBuilder()
        button = InlineKeyboardButton(
            text="Смотреть отзывы",
            url=parse.product.get_product_reviews_link())
        builder.add(button)
        markup = builder.as_markup()
    else:
        markup = None

    await message.answer_photo(photo, caption=ans, parse_mode='Markdown', reply_markup=markup)

@dp.message()
async def answer(message: Message):
    await message.answer('Извини, я тебя не понимаю :с\nПожалуйста, напиши текстовый запрос')

if __name__ == '__main__':
    dp.run_polling(bot)