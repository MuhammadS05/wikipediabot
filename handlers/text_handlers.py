from telebot.types import Message, ReplyKeyboardRemove
from keyboards.default import wiki_btn
import wikipedia

from loader import bot

wikipedia.set_lang("uz")


@bot.message_handler(commands=['start', 'help'])
def reaction_to_commands(message: Message):
    chat_id = message.chat.id
    if message.text == '/start':
        text = f"Salom, {message.from_user.first_name}"
        markup = wiki_btn()
    else:
        text = "Savollar bo'yicha adminga murojat qiling."
        markup = None
    bot.send_message(chat_id, text, reply_markup=markup)


@bot.message_handler(regexp='🔍Wikipedia🔎')
def reaction_to_wiki(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Wikipediadan qanday ma'lumotni olmoqchisiz?",
                           reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_info)


def get_info(message: Message):
    chat_id = message.chat.id
    try:
        sorov = message.text
        wikisorov = wikipedia.summary(sorov, sentences=20)
        bot.send_message(chat_id, wikisorov, reply_markup=wiki_btn())
    except Exception as e:
        print(e, e.__class__)
        bot.send_message(chat_id, f"Siz ma'lumotni noto'g'ri formatda kiritdingiz!", reply_markup=wiki_btn())


