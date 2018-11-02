#!/usr/bin/env python3
import random


# For now, quotes are stored in txt file

def random_quote(quotes):
    """
    random_quote(quotes) - returns random quota from dict of quotes

    Arguments:
    - quotes - dict of quotes
    """
    try:
        return random.choice(quotes)
    except IndexError:
        print('Quotes dict is empty')

x = random_quote({0: 'test1', 1 : 'test2'})
print(x)