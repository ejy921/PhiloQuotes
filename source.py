import json5
import numpy as np
from sklearn.neighbors import NearestNeighbors

QUOTENUM = 128 # Number of quotes in json file.

# Load the quotes data from the JSON file
# List of all the characteristics
characteristics = [
    "Analytical", "Inquisitive", "Modern", "Pragmatic", "Empathetic", 
    "Skeptical", "Introspective", "Philosophical", "Visionary", "Creative", 
    "Spiritual", "Challenging", "Hopeful", "Uplifting"
]

central_characteristics = ["Analytical", "Empathetic", "Visionary"]

other_characteristics = {
    "Inquisitive": [1, 0, 1],
    "Modern": [1, 0, 1],
    "Pragmatic": [1, 1, 0],
    "Skeptical": [1, 0, 0],
    "Introspective": [1, 1, 0],
    "Philosophical": [1, 1, 0],
    "Creative": [0, 0, 1],
    "Spiritual": [0, 1, 1],
    "Challenging": [1, 0, 1],
    "Hopeful": [0, 1, 1],
    "Uplifting": [0, 1, 0],
}

# Load data
with open('quotes.json', 'r') as f:
  quotes_data = json5.load(f)

# Initialize likes/dislikes for each quote
likes_dislikes = {quote['_id']: {'rating': 0} for quote in quotes_data}

def like(item):
  if item in likes_dislikes:
    likes_dislikes[item]['rating'] += 1
  else:
    print(f"Item '{item}' not found.")
feature_vectors = []
quote_texts = []

# Iteration over each quote
for quote in quotes_data:
  
  feature_vector = [0] * len(central_characteristics)

  if 'characteristic' in quote:
    characteristics = quote['characteristic'].split(',')
    for char in characteristics:
      if char in central_characteristics:
        index = central_characteristics.index(char)
        feature_vector[index] += 1
    
      if char in other_characteristics:
        feature_vector += np.array(other_characteristics[char])

    feature_vector = np.array(feature_vector)
    feature_vectors.append(feature_vector)
    quote_texts.append(quote['quote'])

feature_vectors = np.array(feature_vectors)

print("Feature Vectors")
for text, vector in zip(quote_texts, feature_vectors):
  print(f"Quote: {text}\nFeature Vector: {vector}\n")

    




def dislike(item):
  if item in likes_dislikes:
    likes_dislikes[item]['rating'] -= 1
  else:
    print(f"Item '{item}' not found.")

# Print the current state
print(QUOTENUM)
