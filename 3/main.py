from config import API_TOKEN
import telebot

bot = telebot.TeleBot(token=API_TOKEN)

user_id = []

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "welcome")
    if message.chat.id not in user_id:
        user_id.append(message.chat_id)
# -> pengecekan apakah user pernah chat dengan bot atau tidak jika ya lanjut jika tidak append user tersbut

@bot.message_handler(commands=['update'])
def send_update(massage):
    for id in user_id:
        bot.send_message(id, "A new product tersedia")
# -> bila user ada di dafta user_id tampilkan send_message

    
bot.polling()