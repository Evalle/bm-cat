class Cache():
    def __init__(self, data_provider):
        self.cache = {}
        self.data_provider = data_provider
        self.refresh()

    def snapshot(self):
        self.data_provider.save(self.cache)

    def get(self, key):
        return self.cache[key]

    def add(self, key, value):
        self.cache[key].update(value)

    def refresh(self):
        all_data = self.data_provider.get_all()
        if all_data:
            self.cache.update(all_data)