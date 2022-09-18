from telebot import TeleBot, types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from data.bot_token import TOKEN

bot = TeleBot(TOKEN)

menu_keyboard = ReplyKeyboardMarkup(True, False)
button1 = KeyboardButton('Маленькое')
button2 = KeyboardButton('Обычное')
button3 = KeyboardButton('Большое')
button4 = KeyboardButton('Нецелое')
menu_keyboard.row(button1, button2).row(button3, button4)

answer_keyboard = ReplyKeyboardMarkup(True, False).add(KeyboardButton('Ответ'))
