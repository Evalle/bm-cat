import json


class DataProvider:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_all(self):
        try:
            with open(self.connection_string, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, TypeError, ValueError) as e:
            print('Could not get data from storage ' + self.connection_string +
                  ':' + str(e))

    def save(self, obj):
        try:
            with open(self.connection_string, 'w') as file:
                json.dump(obj, file)
        except FileNotFoundError as e:
            print('Not such file:' + str(e))
