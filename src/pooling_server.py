from src.config import BMCAT_APIKEY, bmcat_bot
from telegram.ext import Updater
from telegram.ext import InlineQueryHandler
from telegram.ext import MessageHandler, Filters

# long pooling telegram bot for testing purposes
updater = Updater(token=BMCAT_APIKEY)
dispatcher = updater.dispatcher


def is_inline(update):
    query = update.inline_query
    return query is not None


def inline_bm(bot, update):
    if is_inline(update):
        bmcat_bot.send_random_video(update, bot)


def text_bm(bot, update):
    if not is_inline(update):
        try:
            bmcat_bot.send_random_video(update, bot)
        except ValueError as err:
            print(err)


inline_handler = InlineQueryHandler(inline_bm)
dispatcher.add_handler(inline_handler)

text_bm_handler = MessageHandler(Filters.text, text_bm)
dispatcher.add_handler(text_bm_handler)
updater.start_polling()

# blocks current thread and allow to terminate updater with current script execution thread
updater.idle()