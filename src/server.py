from src import hostbuilder
from src.config import BMCAT_APIKEY, WEBHOOK_URLBASE, WEBHOOK_URLPATH, BMCAT_SSLCERT_PATH, WEBHOOK_LISTEN,\
    BMCAT_PRIVATEKEY_PATH, PORT, app, bot
from telegram.ext import Updater

# webserver entry point
if __name__ == "__main__":
    updater = Updater(BMCAT_APIKEY)

    if bot is None:
        raise ValueError('Telegram bot is not initialized')
        sys.exit(1)

    # delete webhook before new assigning
    bot.deleteWebhook()

    # set new webhook
    bot.setWebhook(WEBHOOK_URLBASE+WEBHOOK_URLPATH, certificate=open(BMCAT_SSLCERT_PATH, 'rb'))
    # build and run server
    hostbuilder.create_host(app).run(host=WEBHOOK_LISTEN,
                                     port=PORT,
                                     ssl_context=(BMCAT_SSLCERT_PATH, BMCAT_PRIVATEKEY_PATH))



