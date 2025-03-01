from config import API_TOKEN
import telebot

bot = telebot.TeleBot(token=API_TOKEN)

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     welcome_text = f'user {message.from_user.first_name} Test berhasil di jalankan'
#     bot.send_message(message.chat.id, welcome_text)
    
# @bot.message_handler(func=lambda message: True)
# def reply_func(message):
#     bot.reply_to(message, text="Ada yang bisa saya bantu?")

# --- bagian sesi 2

# @bot.message_handler(content_types=['audio','document'])
# def handle_audio_doc(massege):
#     if massege.audio:
#         bot.reply_to(massege, "ini adalah audio file")
#     elif massege.document:
#         bot.reply_to(massege, "ini adalah document file")
#  -> ini adalah pengecekan audio dan document  berdasarkan kiriman file dari user

@bot.message_handler(regexp="2025")
def handle_massege(massege):
    bot.reply_to(massege, "Chat anda mengandung '2025'.")
# -> pengecekan per chat bila mengandung data regexp dari chat user

# @bot.message_handler(func=lambda m: m.document.mime_type == 'text/plain', content_types=['document'])
# def handle_text_doc(massege):
#     bot.reply_to(massege, "Ini adalah text file") 
# -> pengecekan type file dengan filter

def test_massege(massege):
    return massege.document.mime_type == 'text/plain'

@bot.message_handler(func=test_massege, content_types=['document'])
def handle_text_doc(massege):
    bot.reply_to(massege, "Ini adalah text file")
# -> mengambil func dari luar handler 

@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda m:m.text == '😂')
def kirim_apa(message):
    bot.reply_to(message, "Emoji Dan Start")
# -> func OR atau pengecekan 2 func


    
bot.polling()