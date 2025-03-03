from config import API_TOKEN
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup

bot = TeleBot(API_TOKEN)

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
reply_keyboard.add("Button1","Button2")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Berikut pilihan yang tersedia", reply_markup=reply_keyboard)
    
@bot.message_handler(func=lambda message:True)
def check_button(message) :
    if message.text == "Button1":
        bot.reply_to(message, "Anda menekan tombol 1.")
    elif message.text == "Button2":
        bot.reply_to(message, "Anda menekan tombol 2.")
    else:
        bot.reply_to(message, f'Message Anda adalah: <b>{message.text}</b>',parse_mode= "HTML")
bot.polling()