from aiogram import Bot, Dispatcher, F
from aiogram.filters import Text, Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
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

@dp.message()
async def search(message: Message):
    query = message.text
    parse = Parser(query)

    parse.parse_ga()
    parse.parse_letual()
    parse.parse_rivgauche()
    ans = make_product_message(query, parse.product.get_product())

    photo = parse.product.get_product_photo()

    await message.answer_photo(photo, caption=ans, parse_mode='Markdown')


if __name__ == '__main__':
    dp.run_polling(bot)