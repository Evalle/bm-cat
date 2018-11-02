from src.data_provider import DataProvider
from src.utils.singleton import Singleton


class Cache(metaclass=Singleton):
    def __init__(self, data_provider):
        self.data_provider = data_provider
        self.cache = self.refresh()

    def snapshot(self):
        self.data_provider.save(self.cache)

    def get(self, key):
        return self.cache[key]

    def add(self, key, value):
        self.cache[key].update(value)

    def refresh(self):
        return self.data_provider.get_all()


storage = '../storage.txt'
c = Cache(DataProvider(storage))
# c.getall()
# c.snapshot()
c.add('quotes', {15: 'test'})
print(c)
