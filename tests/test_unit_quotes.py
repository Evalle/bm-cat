from unittest.mock import MagicMock

from src import quotes
from src.data_provider import DataProvider


def test_quote_should_be_none_for_empty_list():
    empty_data = DataProvider('')
    empty_data.get_all = MagicMock(return_value=[])
    quote = quotes.random_quote(empty_data)
    assert quote is None


def test_quote_should_be_in_array():
    fake_data = DataProvider('')
    qts = ['quote' + str(x) for x in range(5)]
    fake_data.get_all = MagicMock(return_value=qts)
    quote = quotes.random_quote(fake_data)
    assert quote in qts
