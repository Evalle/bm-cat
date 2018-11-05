import unittest
from src import quotes
from src.cache import Cache
from src.data_provider import DataProvider
from src.utils.singleton import Singleton


class QuotesIntegrationTestCase(unittest.TestCase):
    """Integration Test for `src/quotes.py`"""
    
    def test_is_quote_in_datasource(self):
        """Is quote in datasource?"""
        Singleton._instances = {}
        quotes_file_provider = DataProvider('storage.txt')
        cache = Cache(quotes_file_provider)
        self.assertIn(quotes.get_random(cache), list(cache.get('quotes').values()))


q = QuotesIntegrationTestCase()
q.test_is_quote_in_datasource()