import random
from typing import Union

from num2words import num2words
from telebot.types import Message
from src.create_bot import bot, menu_keyboard, answer_keyboard


@bot.message_handler(commands=['start'])
def start_message(message: Message):
    msg = bot.send_message(message.chat.id, 'Приятной тренировки! <3', reply_markup=menu_keyboard)
    bot.register_next_step_handler(msg, menu)


@bot.message_handler(content_types=['text'])
def menu(message: Message):
    if message.text == 'Маленькое':
        num = random.randint(0, 99)
        action = bot.send_message(message.chat.id, f'{num}', reply_markup=answer_keyboard)
        bot.register_next_step_handler(action, cardinal, num)
    elif message.text == 'Обычное':
        num = random.randint(0, 9999)
        action = bot.send_message(message.chat.id, f'{num}', reply_markup=answer_keyboard)
        bot.register_next_step_handler(action, noncardinal, num)
    elif message.text == 'Большое':
        num = random.randint(99, 999999999)
        action = bot.send_message(message.chat.id, f'{"{:,}".format(num)}', reply_markup=answer_keyboard)
        bot.register_next_step_handler(action, cardinal, num)
    elif message.text == 'Нецелое':
        num = random.randint(0, 9999) + round(random.random(), 2)
        action = bot.send_message(message.chat.id, f'{num}', reply_markup=answer_keyboard)
        bot.register_next_step_handler(action, cardinal, num)


@bot.message_handler(content_types=['text'])
def cardinal(message: Message, num: Union[int, float]):
    reply = num2words(num)
    action = bot.send_message(message.chat.id, f'{reply}', reply_markup=menu_keyboard)
    bot.register_next_step_handler(action, menu)


@bot.message_handler(content_types=['text'])
def noncardinal(message: Message, num: Union[int, float]):
    if num2words(num, to='cardinal') == num2words(num, to='year'):
        reply = num2words(num)
    else:
        reply = f"{num2words(num, to='year')}\n" \
                f"({num2words(num)})"
    action = bot.send_message(message.chat.id, f'{reply}', reply_markup=menu_keyboard)
    bot.register_next_step_handler(action, menu)


if __name__ == '__main__':
    bot.infinity_polling()
