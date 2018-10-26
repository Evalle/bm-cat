import hostbuilder
from src.config import TOKEN, WEBHOOK_URLBASE, WEBHOOK_URLPATH, CERTIFICATE_PATH, WEBHOOK_LISTEN,\
    PRIVATEKEY_PATH, PORT, app, bot
from telegram.ext import Updater

# webserver entry point
if __name__ == "__main__":
    updater = Updater(TOKEN)

    # delete webhook before new assigning
    bot.deleteWebhook()

    # set new webhook
    bot.setWebhook(WEBHOOK_URLBASE+WEBHOOK_URLPATH, certificate=open(CERTIFICATE_PATH, 'rb'))
    # build and run server
    hostbuilder.create_host(app).run(host=WEBHOOK_LISTEN,
                                     port=PORT,
                                     ssl_context=(CERTIFICATE_PATH, PRIVATEKEY_PATH))



