import telebot

TOKEN = "8366100206:AAHN9Np0X50cuvB4lNq_n8Hq07YPe4j0x3I"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda msg: True)
def autoreply(message):
    bot.reply_to(message, "Hello! Your message has been received.")

print("Bot is running...")
bot.infinity_polling()
