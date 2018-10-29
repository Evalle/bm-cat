#!/usr/bin/env python3
import random


# For now, quotes are stored in txt file

def random_quote(data_provider):
    """
    random_quote(data_provider) - returns random quota from some data source

    Arguments:
    - data_provider - some data source
    """
    quotes = data_provider.get_all()

    return random.choice(quotes)
