from os import environ
from src.data_provider import DataProvider
from src.bm_cat_bot import BMCatBot
from flask import Flask

PORT = int(environ.get('PORT', '5000'))
BMCAT_HOST = environ.get('BM_CAT_HOST', '')
BMCAT_PORT = int(environ.get('BM_CAT_PORT', '8443'))
WEBHOOK_LISTEN = '0.0.0.0'
WEBHOOK_URLBASE = "https://%s:%s" % (BMCAT_HOST, BMCAT_PORT)

BMCAT_APIKEY = environ.get('BM_CAT_API_KEY', 'api_key_stab')
WEBHOOK_URLPATH = "/%s" % BMCAT_APIKEY

BMCAT_SSLCERT_PATH = environ.get('BM_CAT_SSL_CERTIFICATE_PATH', '')
BMCAT_PRIVATEKEY_PATH = environ.get('BM_CAT_PRIVATE_KEY_PATH', '')

app = Flask(__name__)

QUOTES = '../quotes.txt'
quotes_file_provider = DataProvider(QUOTES)

bmcat_bot = BMCatBot(BMCAT_APIKEY, quotes_file_provider)
