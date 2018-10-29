from src.config import BMCAT_APIKEY
from telegram.ext import Updater, MessageHandler, Filters


# long pooling telegram bot for testing purposes
updater = Updater(token=BMCAT_APIKEY)
dispatcher = updater.dispatcher


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()

# blocks current thread and allow to terminate updater with current script execution thread
updater.idle()
