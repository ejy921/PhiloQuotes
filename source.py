import json5
import numpy as np
from sklearn.neighbors import NearestNeighbors

QUOTENUM = 128 # Number of quotes in json file.

# Load the quotes data from the JSON file
with open('quotes.json', 'r') as f:
  quotes_data = json5.load(f)

# Initialize likes/dislikes for each quote
likes_dislikes = {quote['_id']: {'rating': 0} for quote in quotes_data}

def like(item):
  if item in likes_dislikes:
    likes_dislikes[item]['rating'] += 1
  else:
    print(f"Item '{item}' not found.")

def dislike(item):
  if item in likes_dislikes:
    likes_dislikes[item]['rating'] -= 1
  else:
    print(f"Item '{item}' not found.")

# Print the current state
print(QUOTENUM)
