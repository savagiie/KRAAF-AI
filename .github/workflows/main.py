import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Token البوت
TOKEN = "8446464704:AAEVInxo7LpXdv5LsgFNDmstjcO4pUui23k"

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f'مرحبًا {user.first_name}! أنا بوت مساعدك.')

def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    update.message.reply_text(f'قلت: {text}')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    logger.info("البوت يعمل...")
    updater.idle()

if __name__ == '__main__':
    main()

