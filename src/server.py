from src import hostbuilder
from src.config import WEBHOOK_URLBASE, WEBHOOK_URLPATH, BMCAT_SSLCERT_PATH, WEBHOOK_LISTEN,\
    BMCAT_PRIVATEKEY_PATH, PORT, app, bmcat_bot

# web server entry point
if __name__ == "__main__":
    try:
        bmcat_bot.set_web_hook(WEBHOOK_URLBASE + WEBHOOK_URLPATH,
                               BMCAT_SSLCERT_PATH)
    except:
        raise ValueError('Telegram bot is not initialized')
        sys.exit(1)

    # build and run server
    hostbuilder.create_host(app).run(
        host=WEBHOOK_LISTEN,
        port=PORT,
        ssl_context=(BMCAT_SSLCERT_PATH, BMCAT_PRIVATEKEY_PATH))