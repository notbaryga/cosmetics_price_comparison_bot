from aiogram import Bot, Dispatcher, F
from aiogram.filters import Text, Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile

import os
#from dotenv import load_dotenv
from parse_product import Parser
from utils import make_product_message

#from keyboards import keyboard_categories, keyboard_menu

#load_dotenv()
API_TOKEN: str = '5952388291:AAEWhe9yVx1eoBCtE5o_ko5aC6b_LP6WE8c' #os.getenv('API_TOKEN')

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# хэндлер на "/start"
@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Привет!')

# хэнд на  "/help"
@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('текст для help')

# @dp.message(Command("random"))
# async def cmd_random(message: Message):
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(
#         text="Нажми меня",
#         callback_data="random_value")
#     )
#     await message.answer(
#         "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
#         reply_markup=builder.as_markup()
#     )
#
# @dp.callback_query(Text("random_value"))
# async def send_random_value(callback: CallbackQuery):
#     await callback.message.answer(str(randint(1, 10)))

@dp.message()
async def search(message: Message):
    query = message.text.replace('"',' ')
    parse = Parser(query)

    parse.parse_letual()
    parse.parse_ga()
    parse.parse_rivgauche()
    parse.parse_irecommend()

    ans = make_product_message(query, parse.product.get_product(), parse.product.get_product_rating())

    if parse.product.get_product_photo() is not None:
        photo = parse.product.get_product_photo()
    else:
        photo = FSInputFile('sadcat.jpg')

    if parse.product.get_product_reviews_link() is not None:
        # markup = InlineKeyboardMarkup()
        # markup.add(InlineKeyboardButton(
        #     text="Смотреть отзывы",
        #     url=parse.product.get_product_reviews_link()))

        markup = InlineKeyboardMarkup()
        markup.inline_keyboard.append([InlineKeyboardButton(
            text="Смотреть отзывы",
            url=parse.product.get_product_reviews_link())])

    else:
        markup = None

    await message.answer_photo(photo, caption=ans, parse_mode='Markdown', reply_markup=markup)

if __name__ == '__main__':
    dp.run_polling(bot)