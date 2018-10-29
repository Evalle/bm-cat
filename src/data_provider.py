import json

connection_string = ''


def get_all():
    with open(connection_string, 'r') as file:
        try:
            return json.load(file)
        except FileNotFoundError:
            print("No such file")


def save(obj):
    with open(connection_string, 'w') as file:
        json.dump(obj, file)
