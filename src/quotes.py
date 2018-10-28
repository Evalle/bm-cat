#!/usr/bin/env python3
import random


# For now, quotes are stored in txt file

def random_quote(data_provider):
    """
    random_quote(filename) - returns random quota from filename

    Arguments:
    - filename - path to file with quotes
    """
    quotes = data_provider.get_all()

    return random.choice(quotes)
