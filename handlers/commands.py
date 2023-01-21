from telebot.types import Message

from loader import bot
from keyboards.default import wiki_btn

@bot.message_handler(commands=['start', 'help'])
def reaction_to_commands(message: Message):
    chat_id = message.chat.id
    if message.text == '/start':
        text = f"Assalomu alaykum {message.from_user.first_name}"
        markup = wiki_btn()
    else:
        text = f"Savollar bo'yicha adminga murojaat qiling."
        markup = None

    bot.send_message(chat_id, text, reply_markup=markup)



