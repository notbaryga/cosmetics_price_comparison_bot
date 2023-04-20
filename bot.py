from aiogram import Bot, Dispatcher, F
from aiogram.filters import Text, Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os
from dotenv import load_dotenv
from parse_product import Parser

#from keyboards import keyboard_categories, keyboard_menu

load_dotenv()
API_TOKEN: str = os.getenv('API_TOKEN')

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
    parse = Parser(message.text)
    parse.parse_ga()
    parse.parse_letual()
    parse.parse_rivgauche()
    ans = ''

   # print(parse.product.get_product())
    for el in parse.product.get_product():
        try:
            for er in el:
                ans += er + '\n' + str(el[er]) + '\n'
        except:
            ans += str(el) + '\n'
        ans += '\n'

    await message.answer(ans)


if __name__ == '__main__':
    dp.run_polling(bot)