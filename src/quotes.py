#!/usr/bin/env python3
import random


# For now, quotes are stored in txt file

def get_random(cache):
    """
    random_quote(cache) - returns random quota from cache

    Arguments:
    - cache - global cache
    """
    try:
        return random.choice(list(cache.get('quotes').values()))
    except IndexError:
        print('Quotes dict is empty')
