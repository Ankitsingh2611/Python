import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler

# Replace YOUR_TOKEN with the token you received from the BotFather
bot = telegram.Bot(token="6280304867:AAGZ_A7x6Fr_fkDvyY8QWo4OTSo8n4kUG5w")

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a bot.")

# Define a function to handle messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Set up the Updater with your bot's token
updater = Updater(token="6280304867:AAGZ_A7x6Fr_fkDvyY8QWo4OTSo8n4kUG5w", use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Add command handlers
dispatcher.add_handler(CommandHandler('start', start))

# Add message handler
#ommand, echo))

# Start polling for updates
updater.start_polling()
