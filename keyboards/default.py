from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def wiki_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    wiki = KeyboardButton('🔍Wikipedia🔎')
    markup.add(wiki)
    return markup


