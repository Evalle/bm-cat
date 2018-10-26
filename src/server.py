import hostbuilder
from src.config import TOKEN, WEBHOOK_URL_BASE, WEBHOOK_URL_PATH, CERTIFICATE_PATH, WEBHOOK_LISTEN,\
    PRIVATE_KEY_PATH, PORT, app, bot
from telegram.ext import Updater

# webserver entry point
if __name__ == "__main__":
    updater = Updater(TOKEN)

    # delete webhook before new assigning
    bot.deleteWebhook()

    # set new webhook
    bot.setWebhook(WEBHOOK_URL_BASE+WEBHOOK_URL_PATH, certificate=open(CERTIFICATE_PATH, 'rb'))
    # build and run server
    hostbuilder.create_host(app).run(host=WEBHOOK_LISTEN,
                                     port=PORT,
                                     ssl_context=(CERTIFICATE_PATH, PRIVATE_KEY_PATH))



