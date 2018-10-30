import json


class DataProvider:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_all(self):
        with open(self.connection_string, 'r') as file:
            try:
                return json.load(file)
            except FileNotFoundError:
                print("No such file")

    def save(self, obj):
        with open(self.connection_string, 'w') as file:
            json.dump(obj, file)
