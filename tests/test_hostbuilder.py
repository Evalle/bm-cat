from src import hostbuilder
import flask
from src import config


def test_post_register_handler():
    """
    should call change_res on POST request
    :return:
    """
    app = flask.Flask(__name__)
    client = app.test_client()
    test_post_register_handler.res = False

    def chage_res():
        test_post_register_handler.res = True

    hostbuilder.register_handler(app, chage_res)

    client.post('/%s' % config.BMCAT_APIKEY)
    assert test_post_register_handler.res


def test_get_register_handler():
    """
    shouldn't call change_res on GET request
    :return:
    """
    app = flask.Flask(__name__)
    client = app.test_client()
    test_get_register_handler.res = False

    def chage_res():
        test_get_register_handler.res = True

    hostbuilder.register_handler(app, chage_res)

    client.get('/%s' % config.BMCAT_APIKEY)
    assert not test_get_register_handler.res
