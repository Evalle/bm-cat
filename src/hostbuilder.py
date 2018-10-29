from src.config import BMCAT_APIKEY, bot
from flask import request

import telegram


def create_host(app):
    """
    configuration point of bm_cat server
    you can do everything with app at this point to build host

    :param app: flask server instance
    :return: app
    """
    register_handler(app, bm_cat_handler)
    return app


def register_handler(app, handler):
    """
    registration of handler for bm_cat bot server
    only POST requests will processed

    :param app: instance of flask server
    :param handler: web request handler
    :return: void
    """
    app.add_url_rule('/' + BMCAT_APIKEY, 'handler', handler, methods=['POST'])


def bm_cat_handler():
    """
    bm_cat_handler() - root handler of bm_cat webhook

    :return: OK - 200
    """
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True), bot=bot)

        chat_id = update.message.chat.id

        text = update.message.text

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'
