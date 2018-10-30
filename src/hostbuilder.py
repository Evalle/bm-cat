from src.config import BMCAT_APIKEY, bmcat_bot
from flask import request

import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent

from src.random_video_request_handler import response_random_video


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
        update = telegram.Update.de_json(request.get_json(force=True), bot=bmcat_bot.get_bot())

        bmcat_bot.send_random_video(update)

    return 'ok'


