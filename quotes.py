#!/usr/bin/env python3
import sys
import random
# For now, quotes are stored in txt file

def random_quote(filename):
  """
  random_quote(filename) - returns random quota from filename

  Arguments:
  - filename - path to file with quotes
  """

  with open(filename, 'r') as inputf:
    try:
      quotes = inputf.read().splitlines()
    except FileNotFoundError:
      print("No such file")
      sys.exit(1)
    
  return random.choice(quotes)
  inputf.close()
  

filename = "quotes.txt"
print(random_quote(filename))

