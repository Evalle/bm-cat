from src.config import BMCAT_APIKEY, bot
from flask import request

import telegram
from src.random_video_request_handler import response_random_video


# server configuration point
def create_host(app):
    register_handler(app, webhook_handler)
    return app


def register_handler(app, handler):
    app.add_url_rule('/' + BMCAT_APIKEY, 'handler', handler, methods=['POST'])


def echo_telegram_response(request, bot):
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot=bot)

    chat_id = update.message.chat.id

    text = update.message.text

    # repeat the same message back (echo)
    bot.sendMessage(chat_id=chat_id, text=text)


# "echo" chatbot
def webhook_handler():
    if request.method == "POST":
        # echo_telegram_response(request, bot)
        update = telegram.Update.de_json(request.get_json(force=True), bot=bot)
        video = response_random_video(update);
        if video is not None:
            bot.send_message(chat_id=update.message.chat.id, text=video)

    return 'ok'
