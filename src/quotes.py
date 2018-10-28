#!/usr/bin/env python3
import sys
import random
import dbcontext
import json


# For now, quotes are stored in txt file

def random_quote(filename):
    """
    random_quote(filename) - returns random quota from filename

    Arguments:
    - filename - path to file with quotes
    """
    dbcontext.connection_string = filename
    quotes = dbcontext.get_all()

    return random.choice(quotes)


filename = "../quotes.txt"
print(random_quote(filename))
