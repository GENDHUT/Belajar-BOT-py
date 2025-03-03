from config import API_TOKEN
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = TeleBot(API_TOKEN)

button1 = InlineKeyboardButton(text="Button1",callback_data="btn1")
button2 = InlineKeyboardButton(text="Button2",callback_data="btn2")
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard.add(button1,button2)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hai ada yang bsia saya bantu?", reply_markup = inline_keyboard)
    
@bot.callback_query_handler(func = lambda call:True)
def test_button(call):
    if call.data == "btn1":
        bot.answer_callback_query(call.id, "ini adalah tombol 1.", show_alert=True)
    elif call.data == "btn2":
        bot.answer_callback_query(call.id, "ini adalah tombol 2.", show_alert=True)

bot.polling()