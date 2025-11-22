import telebot

TOKEN = "YOUR_TELEGRAM_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda msg: True)
def autoreply(message):
    bot.reply_to(message, "Hello! Your message has been received.")

print("Bot is running...")
bot.infinity_polling()
