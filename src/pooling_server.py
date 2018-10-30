from src.config import BMCAT_APIKEY
from src import random_video_request_handler, quotes, data_provider
from telegram.ext import Updater, MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler


# long pooling telegram bot for testing purposes
updater = Updater(token=BMCAT_APIKEY)
dispatcher = updater.dispatcher
data_provider.connection_string = '../quotes.txt'


def inline_bm(bot, update):
    query = update.inline_query.query
    if not query:
        return
    video_link = random_video_request_handler.response_random_video(update)
    if video_link is None:
        return
    random_quote = quotes.random_quote(data_provider)
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title=random_quote,
            input_message_content=InputTextMessageContent('%s\n\r%s' % (random_quote, video_link))
        )
    )
    # 10 seconds cache
    bot.answer_inline_query(update.inline_query.id, results, cache_time=10)


inline_caps_handler = InlineQueryHandler(inline_bm)
dispatcher.add_handler(inline_caps_handler)
updater.start_polling()

# blocks current thread and allow to terminate updater with current script execution thread
updater.idle()
