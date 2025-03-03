from config import API_TOKEN
from telebot import TeleBot

bot = TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "welcome ada yang bisa saya bantu?")
    
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for new_member in message.new_chat_member:
        welcome_text = f'😍 {message.from_user.fist_name}, Selamat datang !!!'
        bot.send_message(message.chat.id, text=welcome_text)
        
def is_user_admin(chat_id,user_id):
    admins = bot.get_chat_administrators(chat_id)
    for admins in admins:
        if admins.user.id == user_id:
            return True
    return False

@bot.message_handler(func=lambda message: message.text == "pin")
def pin_massage(massage):
    chat_id = massage.chat.id
    user_id = massage.from_user.id
    
    if is_user_admin(chat_id,user_id):
        if massage.reply_to_message:
            bot.pin_chat_message(chat_id, massage.reply_to_message.message_id)
            bot.reply_to(massage.reply_to_message, "Message berhasil di pin!")
        else:
            bot.reply_to(massage.reply_to_message, "pilih massage anda sebelum pin!")
    else:
        bot.reply_to(massage.chat.id, "Hanya admin yang dapat membuat pin massage!")


            
    

bot.polling()