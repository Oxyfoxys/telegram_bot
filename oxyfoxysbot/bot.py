import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    # Создаем клавиатуру и каждую из кнопок (по 2 в ряд)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    url_button = types.InlineKeyboardButton(text="URL", url="https://stihi.ru/photos/steelrat222.jpg")
    callback_button = types.InlineKeyboardButton(text="Callback", callback_data="test")
    switch_button = types.InlineKeyboardButton(text="Switch", switch_inline_query="Telegram")
    keyboard.add(url_button, callback_button, switch_button)
    bot.send_message(message.chat.id, "Я – пофырчу немного", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Фыр")
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Фыр")

if __name__ == '__main__':
     bot.infinity_polling()


