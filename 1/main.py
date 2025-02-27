from config import API_TOKEN
import telebot

bot = telebot.TeleBot(token=API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = f'user {message.from_user.first_name} Test berhasil di jalankan'
    bot.send_message(message.chat.id, welcome_text)
    
@bot.message_handler(func=lambda message: True)
def reply_func(message):
    bot.reply_to(message, text="Ada yang bisa saya bantu?")
    
bot.polling()