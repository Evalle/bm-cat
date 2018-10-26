from os import environ
import telegram
from flask import Flask

PORT = int(environ.get('PORT', '5000'))
WEBHOOK_HOST = environ['BM_CAT_HOST']
WEBHOOK_PORT = int(environ.get('BM_CAT_PORT', '8443'))
WEBHOOK_LISTEN = '0.0.0.0'
WEBHOOK_URLBASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)

TOKEN = environ['BM_CAT_API_KEY']
WEBHOOK_URLPATH = "/%s" % TOKEN

CERTIFICATE_PATH = environ['BM_CAT_SSL_CERTIFICATE_PATH']
PRIVATEKEY_PATH = environ['BM_CAT_PRIVATE_KEY_PATH']

app = Flask(__name__)

global bot
bot = telegram.Bot(token=TOKEN)
