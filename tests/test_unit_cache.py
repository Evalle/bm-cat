from unittest.mock import MagicMock

import unittest

from src.cache import Cache
from src.data_provider import DataProvider
from src.utils.singleton import Singleton


class CacheTest(unittest.TestCase):
    some_data = {'test': {0: 'test1', 1: 'test2'},
                 'test1': {5: 'test2', 10: 'test3'}}
    data_provider = DataProvider('fake_data')

    def test_cache_is_singleton(self):
        Singleton._instances = {}
        self.data_provider.get_all = MagicMock(return_value=self.some_data)
        cache1 = Cache(self.data_provider)

        empty_data = DataProvider('empty_data')
        empty_data.get_all = MagicMock(return_value={})
        cache2 = Cache(empty_data)
        self.assertDictEqual(cache1.cache, cache2.cache)

    def test_cache_should_call_refresh_after_initialize(self):
        Singleton._instances = {}
        self.data_provider.get_all = MagicMock(return_value=self.some_data)
        cache = Cache(self.data_provider)
        self.assertDictEqual(self.some_data, cache.cache)

    def test_cache_get_should_return_value(self):
        Singleton._instances = {}
        self.data_provider.get_all = MagicMock(return_value=self.some_data)
        cache = Cache(self.data_provider)
        self.assertDictEqual(cache.get('test'), self.some_data['test'])

    def test_cache_snapshot_call_once(self):
        Singleton._instances = {}
        fake_data = DataProvider('')
        fake_data.get_all = MagicMock(return_value={'test': 1})
        fake_data.save = MagicMock()
        cache = Cache(fake_data)
        cache.snapshot()
        fake_data.save.assert_called_once()
