from src.config import TOKEN, bot
from flask import request

import telegram


# server configuration point
def create_host(app):
    register_handler(app, webhook_handler)
    return app


def register_handler(app, handler):
    app.add_url_rule('/' + TOKEN, 'handler', handler, methods=['POST'])


# "echo" chatbot
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True), bot=bot)

        chat_id = update.message.chat.id

        text = update.message.text

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'
