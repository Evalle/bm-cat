import unittest
import json
from src import quotes
from src.data_provider import DataProvider

class QuotesIntegrationTestCase(unittest.TestCase):
    """Integration Test for `src/quotes.py`"""
    
    def test_is_quote_in_datasource(self):
        """Is quote in datasource?"""

        datasource = "quotes.txt"
        quotes_file_provider = DataProvider(datasource)
        data_list = json.load(open(datasource, "r"))
        self.assertIn(quotes.random_quote(quotes_file_provider), data_list)

if __name__ == '__main__':
    unittest.main()