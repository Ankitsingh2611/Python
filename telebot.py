import telebot
import requests
bot=telebot.TeleBot("6249215249:AAGnR6Yp_GskgJB65FPbVLbyZoNC6iKUyhU")
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,"Hello,welcome hihahahaha")
    bot.polling()