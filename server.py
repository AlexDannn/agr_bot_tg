import logging
from aiogram import Bot, Dispatcher, executor, types 
from scrap import *
import os

from middleswares import AccessMiddleware

API_TOKEN = os.getenv('API_TOKEN')
ACCESS_ID = os.getenv('ACCESS_ID')

#Configure logging
logging.basicConfig(level=logging.INFO)

#Initialize bot and dispatcher 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(ACCESS_ID))

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Good ebening!\nI'm scrap Bot.\nPowered by aiogram")


#@dp.message_handler(commands=['sport'])
#async def send_sports(message: types.Message):
#    example = sports_rss()
#    answer_message = ""
#    for i in example:
#        answer_message += i.get('title') + '\n' + i.get('link') + '\n' + '\n'
#    await message.answer(answer_message)

@dp.message_handler(commands=['games'])
async def send_games(message: types.Message):
    example = games_rss()
    answer_message = ""
    for i in example:
        answer_message += i.get('title') + '\n' + i.get('link') + '\n' + '\n'
    await message.answer(answer_message)

@dp.message_handler(commands=['movies'])
async def send_movies(message: types.Message):
    example = movies_rss()
    answer_message = ""
    for i in example:
        answer_message += i.get('title') + '\n' + i.get('link') + '\n' + '\n'
    await message.answer(answer_message)

@dp.message_handler(commands=['hacks'])
async def send_hacks(message: types.Message):
    example = hacks_rss()
    answer_message = ""
    for i in example:
        answer_message += i.get('title') + '\n' + i.get('link') + '\n' + '\n'
    await message.answer(answer_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


example1 = sports_rss()
#example2 = games_rss()
#example3 = hackernews_rss()
#example4 = movies_rss()

print(example1)
#print(example2)
#print(example3)
#print(example4)